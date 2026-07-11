from src.config.database import supabase
from src.schemas.abastecimiento_schema import AbastecimientoCreate
from src.schemas.venta_schema import VentaCreate,VentaResponse
from fastapi import HTTPException, status

class InventarioService:

    @staticmethod
    def registrar_abastecimiento(abastecimiento: AbastecimientoCreate):
        prod_resp = supabase.table("producto").select("id_producto", "stock").eq("id_producto", abastecimiento.id_producto).execute()
        if not prod_resp.data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No se puede abastecer: El producto con ID {abastecimiento.id_producto} no existe"
            )
        
        producto_actual = prod_resp.data[0]
        stock_actual = producto_actual["stock"]

        prov_resp = supabase.table("proveedor").select("id_proveedor").eq("id_proveedor", abastecimiento.id_proveedor).execute()
        if not prov_resp.data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"El proveedor con ID {abastecimiento.id_proveedor} no está registrado"
            )

        user_resp = supabase.table("usuario").select("id_usuario").eq("id_usuario", abastecimiento.id_usuario).execute()
        if not user_resp.data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"El usuario con ID {abastecimiento.id_usuario} no existe"
            )

        data_abastecimiento = abastecimiento.model_dump()
        abast_resp = supabase.table("abastecimiento").insert(data_abastecimiento).execute()
        
        if not abast_resp.data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="No se pudo procesar el registro de abastecimiento"
            )

        nuevo_stock = stock_actual + abastecimiento.cantidad
        supabase.table("producto").update({"stock": nuevo_stock}).eq("id_producto", abastecimiento.id_producto).execute()

        return abast_resp.data[0]

    @staticmethod
    def obtener_historial_abastecimientos():
        response = supabase.table("abastecimiento").select("*").order("created_at", desc=True).execute()
        return response.data
    
    @staticmethod
    def registrar_venta(venta:VentaCreate):
        total_calculado=0.0
        productos_verificados=[]
        
        for item in venta.productos:
            prod_resp=supabase.table("producto").select("id_producto","stock","nombre").eq("id_producto",item.id_producto).execute()
            if not prod_resp.data:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"El producto con el ID {item.id_producto} no existe"
                )
            producto_bd = prod_resp.data[0]
            
            if producto_bd["stock"] < item.cantidad:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Stock insuficiente para '{producto_bd['nombre']}'. Disponible: {producto_bd['stock']}"
                )
            total_calculado += item.cantidad * item.precio_unitario
            
            productos_verificados.append({
                "id_producto":item.id_producto,
                "stock_actual":producto_bd["stock"],
                "cantidad_vendida":item.cantidad,
                "datos_detalle":item.model_dump()
            })

        data_venta={
            "id_usuario":venta.id_usuario,
            "total":total_calculado
        }
        
        venta_resp=supabase.table("venta").insert(data_venta).execute()
        if not venta_resp.data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No se pudo registrar la cabecera de venta"
                )
        nueva_venta=venta_resp.data[0]
        id_nueva_venta=nueva_venta["id_venta"]
        
        detalles_creados=[]
        
        for prod in productos_verificados:
            detalle_dict=prod["datos_detalle"]
            detalle_dict["id_venta"]=id_nueva_venta
            
            det_resp=supabase.table("detalle_venta").insert(detalle_dict).execute()
            if det_resp.data:
                detalles_creados.append(det_resp.data[0])

            nuevo_stock= prod["stock_actual"] - prod["cantidad_vendida"]
            supabase.table("producto").update({"stock":nuevo_stock}).eq("id_producto", prod["id_producto"]).execute()
            
        
        respuesta={
            "id_usuario": nueva_venta["id_usuario"],
            "id_venta": nueva_venta["id_venta"],
            "total": nueva_venta["total"],
            "created_at": nueva_venta["created_at"],
            "productos": detalles_creados
        }
        
        return respuesta
          
    @staticmethod
    def obtener_historial_ventas():
        response= supabase.table("venta").select("*").order("id_venta",desc=True).execute()
        return response.data