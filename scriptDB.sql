CREATE TABLE categoria (
    id_categoria SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE usuario (
    id_usuario SERIAL PRIMARY KEY,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE proveedor (
    id_proveedor SERIAL PRIMARY KEY,
    ruc VARCHAR(20) UNIQUE NOT NULL,
    razon_social VARCHAR(150) NOT NULL,
    telefono VARCHAR(20),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE producto (
    id_producto SERIAL PRIMARY KEY,
    sku VARCHAR(50) UNIQUE NOT NULL,
    nombre VARCHAR(150) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT DEFAULT 0,
    id_categoria INT REFERENCES categoria(id_categoria) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE abastecimiento (
    id_abastecimiento SERIAL PRIMARY KEY,
    cantidad INT NOT NULL,
    precio_compra DECIMAL(10, 2) NOT NULL,
    id_proveedor INT REFERENCES proveedor(id_proveedor) ON DELETE RESTRICT,
    id_usuario INT REFERENCES usuario(id_usuario) ON DELETE RESTRICT,
    id_producto INT REFERENCES producto(id_producto) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE venta (
    id_venta SERIAL PRIMARY KEY,
    total DECIMAL(10, 2) DEFAULT 0,
    id_usuario INT REFERENCES usuario(id_usuario) ON DELETE RESTRICT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE TABLE detalle_venta (
    id_detalle_venta SERIAL PRIMARY KEY,
    id_venta INT REFERENCES venta(id_venta) ON DELETE CASCADE,
    id_producto INT REFERENCES producto(id_producto) ON DELETE RESTRICT,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10, 2) NOT NULL
);