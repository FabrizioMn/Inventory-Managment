# 📦 Sistema de Gestión de Inventario y Proveedores (Backend)

La aplicación está construida como una **API REST** modular utilizando Python, diseñada especialmente para ser consumida de forma eficiente por un frontend en **React**.

---

## 🚀 Tecnologías Utilizadas

* **[Python 3.10+]** - Lenguaje principal de desarrollo.
* **[FastAPI]** - Framework web moderno, de alto rendimiento y con documentación interactiva automática.
* **[Supabase / PostgreSQL]** - Base de datos relacional en la nube y cliente de gestión de datos.
* **[Pydantic]** - Validación estricta de datos y tipado para seguridad de la API.
* **[Uvicorn]** - Servidor ASGI rápido para correr la aplicación.

---

## 📁 Arquitectura del Proyecto

El proyecto sigue una estructura **Modular por Capas** para separar la lógica de negocio de los accesos a datos y los endpoints:

```text
mi_proyecto_inventario/
├── app/
│   ├── config/       # Configuración y cliente de Supabase
│   ├── routes/       # Endpoints de la API
│   ├── schemas/      # Validadores de entrada/salida
│   ├── services/     # Lógica de negocio 
│   └── main.py       # Punto de entrada de la aplicación
├── .env              # Variables de entorno
├── requirements.txt  # Dependencias del proyecto
└── README.md         # Documentación