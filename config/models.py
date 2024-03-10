from typing import List
from typing import Optional
from sqlalchemy import ForeignKey, Integer,Date,Numeric
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base =declarative_base()
metadata = Base.metadata


class Base(DeclarativeBase):
    pass

class ROl(Base):
    """
    Representa el modelo de la tabla ROl
    """
    __tablename__ = 'rol'
    id:Mapped[int] = mapped_column(Integer, primary_key=True,autoincrement="auto")
    nombre:Mapped[str] = mapped_column(String(50),nullable=False) 
    grupo_rol_permisos:Mapped["GRUPO_ROL_PERMISOS"] = relationship("GRUPO_ROL_PERMISOS", back_populates="rol", cascade="all, refresh-expire")
    def __repr__(self):
        return f"Rol(id={self.id}, nombre={self.nombre})"

class PERMISOS(Base):
    """
    Representa el modelo de la tabla PERMISOS
    """
    __tablename__ = 'permisos'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement="auto")
    nombre:Mapped[str] = mapped_column(String(50), nullable=False)
    grupopermisos_permisos:Mapped["GRUPOPERMISOS_PERMISOS"] = relationship("GRUPOPERMISOS_PERMISOS", back_populates="permisos", cascade="all, refresh-expire")

    def __repr__(self):
        return f"PERMISOS(id={self.id}, nombre={self.nombre})"

class GRUPO_DE_PERMISOS(Base):
    """
    Representa el modelo de la tabla GRUPO_DE_PERMISOS
    """
    __tablename__ = 'grupo_de_permisos'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement="auto")
    nombre:Mapped[str] = mapped_column(String(50), nullable=False)
    permisos_asociados: Mapped[List["GRUPOPERMISOS_PERMISOS"]] = relationship("GRUPOPERMISOS_PERMISOS", back_populates="grupopermisos", cascade="all, refresh-expire")    
    def __repr__(self):
        return f"GRUPO_DE_PERMISOS(id={self.id}, nombre={self.nombre})"
    
class GRUPOPERMISOS_PERMISOS(Base):
    """
    Representa el modelo de la tabla GRUPOPERMISOS_PERMISOS
    """
    __tablename__ = 'grupopermisos_permisos'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement="auto")
    grupopermisos_id:Mapped[int] = mapped_column(Integer, ForeignKey('grupo_de_permisos.id'))
    permisos_id:Mapped[int] = mapped_column(Integer, ForeignKey('permisos.id'))
    grupopermisos:Mapped["GRUPO_DE_PERMISOS"] = relationship("GRUPO_DE_PERMISOS", back_populates="permisos_asociados",cascade="all,refresh-expire")
    permisos:Mapped[List["PERMISOS"]] = relationship("PERMISOS", back_populates="grupopermisos_permisos",cascade="all,refresh-expire")
    grupo_rol_permisos:Mapped["GRUPO_ROL_PERMISOS"] = relationship("GRUPO_ROL_PERMISOS", back_populates="grupopermisos_permisos", cascade="all, refresh-expire")

class GRUPO_ROL_PERMISOS(Base):
    """
    Representa el modelo de la tabla GRUPO_ROL_PERMISOS
    """
    __tablename__ = 'grupo_rol_permisos'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement="auto")
    gruporol_id:Mapped[int] = mapped_column(Integer, ForeignKey('grupopermisos_permisos.id'))
    grupopermisos_permisos:Mapped["GRUPOPERMISOS_PERMISOS"] = relationship("GRUPOPERMISOS_PERMISOS", back_populates="grupo_rol_permisos", cascade="all, refresh-expire")
    rol_id:Mapped[int] = mapped_column(Integer, ForeignKey('rol.id'))
    rol:Mapped["ROl"] = relationship("ROl", back_populates="grupo_rol_permisos", cascade="all, refresh-expire")
    usuarios:Mapped["USUARIOS"] = relationship("USUARIOS", back_populates="grupo_rol_permisos", cascade="all, refresh-expire")

class TIPO_DE_DOCUMENTO(Base):
    """
    Representa el modelo de la tabla TIPO_DE_DOCUMENTO
    """
    __tablename__ = 'tipo_de_documento'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement="auto")
    nombre:Mapped[str] = mapped_column(String(50), nullable=False)
    cliente:Mapped["CLIENTES"] = relationship("CLIENTES", back_populates="tipo_de_documento", cascade="all, refresh-expire")
    def __repr__(self):
        return f"TIPO_DE_DOCUMENTO(id={self.id}, nombre={self.nombre})"

class IMAGEN_USUARIO(Base):
    """
    Representa el modelo de la tabla IMAGEN_USUARIO
    """
    __tablename__ = 'imagen_usuario'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement="auto")
    url:Mapped[str] = mapped_column(String(50), nullable=False)
    usuarios_imagen:Mapped["CLIENTES"] = relationship("CLIENTES", back_populates="url_imagen", cascade="all, refresh-expire")
    
class CLIENTES(Base):
    """
    Representa el modelo de la tabla CLIENTES
    """
    __tablename__ = 'clientes'
    cliente_id:Mapped[int] = mapped_column(Integer, primary_key=True,nullable=False)
    nombre:Mapped[str] = mapped_column(String(50), nullable=False)
    apellido:Mapped[str] = mapped_column(String(50), nullable=False)
    email:Mapped[str] = mapped_column(String(50), nullable=False)
    telefono:Mapped[List[int]] = mapped_column(Integer, nullable=True)
    celular:Mapped[List[int]] = mapped_column(Integer, nullable=True)
    direccion:Mapped[List[str]] = mapped_column(String(100), nullable=True)
    fechaNacimiento:Mapped[Date] = mapped_column(Date, nullable=True)
    tipo_de_documento_id:Mapped[int] = mapped_column(Integer, ForeignKey('tipo_de_documento.id'))
    tipo_de_documento:Mapped["TIPO_DE_DOCUMENTO"] = relationship("TIPO_DE_DOCUMENTO", back_populates="cliente", cascade="all, refresh-expire")
    url_imagen:Mapped[Optional["IMAGEN_USUARIO"]] = relationship("IMAGEN_USUARIO", back_populates="usuarios_imagen", cascade="all, refresh-expire")
    url_imagen_id:Mapped[int]= mapped_column(Integer, ForeignKey('imagen_usuario.id'))
    usuarios_id:Mapped[int]= mapped_column(Integer, ForeignKey('usuarios.id'))
    usuarios:Mapped["USUARIOS"] = relationship("USUARIOS", back_populates="cliente", cascade="all, refresh-expire",uselist=False)
    det_pedido:Mapped["DET_PEDIDO"] = relationship("DET_PEDIDO", back_populates="cliente", cascade="all, refresh-expire")
    metodo_pago:Mapped["METODOS_PAGO"] = relationship("METODOS_PAGO", back_populates="cliente", cascade="all, refresh-expire",uselist=False)
class USUARIOS(Base):
    """
    Representa el modelo de la tabla USUARIOS
    """
    __tablename__ = 'usuarios'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement="auto")
    nombre:Mapped[str] = mapped_column(String(50), nullable=False)
    contrasena:Mapped[str] = mapped_column(String(255), nullable=False)
    cliente = relationship("CLIENTES", back_populates="usuarios", cascade="all, refresh-expire",uselist=False)
    grupo_rol_permisos_id:Mapped[int] = mapped_column(Integer, ForeignKey('grupo_rol_permisos.id'))
    grupo_rol_permisos:Mapped["GRUPO_ROL_PERMISOS"] = relationship("GRUPO_ROL_PERMISOS", back_populates="usuarios", cascade="all, refresh-expire")

    def __repr__(self):
        return f"USUARIOS(id={self.id}, nombre={self.nombre}, contrasena={self.contrasena}, cliente_id={self.cliente_id}, grupo_rol_permisos_id={self.grupo_rol_permisos_id})"

class TARJETAS(Base):
    """
    Representa el modelo de la tabla TARJETAS
    """
    __tablename__ = 'tarjetas'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement="auto")
    numero:Mapped[int] = mapped_column(Integer, nullable=False)
    fecha_vencimiento:Mapped[Date] = mapped_column(Date, nullable=False)
    cvv:Mapped[int] = mapped_column(Integer, nullable=False)
    monto:Mapped[Numeric] = mapped_column(Numeric, nullable=False)
    metodos_pago:Mapped["METODOS_PAGO"] = relationship("METODOS_PAGO", back_populates="tarjetas", cascade="all, refresh-expire",uselist=False)
    def __repr__(self):
        return f"TARJETAS(id={self.id}, numero={self.numero}, fecha_vencimiento={self.fecha_vencimiento}, cvv={self.cvv}, monto={self.monto})"

class PAYPAL(Base):
    """
    Representa el modelo de la tabla PAYPAL
    """
    __tablename__ = 'paypal'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement="auto")
    email:Mapped[str] = mapped_column(String(50))
    monto:Mapped[Numeric] = mapped_column(Numeric, nullable=False)
    metodos_pago:Mapped["METODOS_PAGO"] = relationship("METODOS_PAGO", back_populates="paypal", cascade="all, refresh-expire",uselist=False)
    def __repr__(self):
        return f"PAYPAL(id={self.id}, email={self.email}, monto={self.monto})"
    
class ESTADO_PAGO(Base):
    """
    Representa el modelo de la tabla ESTADO_PAGO
    """
    __tablename__ = 'estado_pago'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement="auto")
    nombre:Mapped[str] = mapped_column(String(50), nullable=False)
    metodos_pago:Mapped["METODOS_PAGO"] = relationship("METODOS_PAGO", back_populates="estado_pago", cascade="all, refresh-expire")
    def __repr__(self):
        return f"ESTADO_PAGO(id={self.id}, nombre={self.nombre})"
    
class METODOS_PAGO(Base):
    """
    Representa el modelo de la tabla METODOS_PAGO
    """
    __tablename__ = 'metodos_pago'
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    cliente_id = mapped_column(Integer, ForeignKey('clientes.cliente_id'))
    fecha_transaccion:Mapped[Date] = mapped_column(Date, nullable=False)
    cliente = relationship("CLIENTES", back_populates="metodo_pago", cascade="all, refresh-expire")
    paypal_id = mapped_column(Integer, ForeignKey('paypal.id'))
    paypal = relationship("PAYPAL", back_populates="metodos_pago", cascade="all, refresh-expire")
    tarjetas_id = mapped_column(Integer, ForeignKey('tarjetas.id'))
    tarjetas = relationship("TARJETAS", back_populates="metodos_pago", cascade="all, refresh-expire")
    estado_pago_id = mapped_column(Integer, ForeignKey('estado_pago.id'))
    estado_pago = relationship("ESTADO_PAGO", back_populates="metodos_pago", cascade="all, refresh-expire")

class MUNICIPIOS(Base):
    """
    Representa el modelo de la tabla MUNICIPIOS
    """
    __tablename__ = 'municipios'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement="auto")
    nombre:Mapped[str] = mapped_column(String(50), nullable=False)
    departamentos:Mapped["DEPARTAMENTOS"] = relationship("DEPARTAMENTOS", back_populates="municipios", cascade="all, refresh-expire")
    def __repr__(self):
        return f"MUNICIPIOS(id={self.id}, nombre={self.nombre})"
class CIUDADES(Base):
    """
    Representa el modelo de la tabla CIUDADES
    """
    __tablename__ = 'ciudades'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement="auto")
    nombre:Mapped[str] = mapped_column(String(50), nullable=False)
    departamentos:Mapped["DEPARTAMENTOS"] = relationship("DEPARTAMENTOS", back_populates="ciudades", cascade="all, refresh-expire")
    def __repr__(self):
        return f"CIUDADES(id={self.id}, nombre={self.nombre})"   
class DEPARTAMENTOS(Base):
    """
    Representa el modelo de la tabla DEPARTAMENTOS
    """
    __tablename__ = 'departamentos'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement="auto")
    nombre:Mapped[str] = mapped_column(String(50), nullable=False)
    municipio_id = mapped_column(Integer, ForeignKey('municipios.id'))
    municipios:Mapped["MUNICIPIOS"] = relationship("MUNICIPIOS", back_populates="departamentos", cascade="all, refresh-expire")
    ciudad_id = mapped_column(Integer, ForeignKey('ciudades.id'))
    ciudades:Mapped["CIUDADES"] = relationship("CIUDADES", back_populates="departamentos", cascade="all, refresh-expire")
    pais:Mapped["PAIS"] = relationship("PAIS", back_populates="departamentos", cascade="all, refresh-expire")
    def __repr__(self):
        return f"DEPARTAMENTOS(id={self.id}, nombre={self.nombre})"
class PAIS(Base):
    """
    Representa el modelo de la tabla PAIS
    """
    __tablename__ = 'pais'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement="auto")
    nombre:Mapped[str] = mapped_column(String(50), nullable=False)
    departamentos:Mapped["DEPARTAMENTOS"] = relationship("DEPARTAMENTOS", back_populates="pais", cascade="all, refresh-expire")
    departamento_id = mapped_column(Integer, ForeignKey('departamentos.id'))
    direccion:Mapped["DIRECCION"] = relationship("DIRECCION", back_populates="pais", cascade="all, refresh-expire")
    def __repr__(self):
        return f"PAIS(id={self.id}, nombre={self.nombre})"
    
class DIRECCION(Base):
    """
    Representa el modelo de la tabla DIRECCION
    """
    __tablename__ = 'direccion'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement="auto")
    calle:Mapped[str] = mapped_column(String(50), nullable=False)
    carrera:Mapped[str] = mapped_column(String(50), nullable=False)
    numero:Mapped[int] = mapped_column(Integer, nullable=False)
    indicador:Mapped[str] = mapped_column(String(50), nullable=False)
    diagonal:Mapped[str] = mapped_column(String(50), nullable=False)
    pais_id:Mapped[int] = mapped_column(Integer,ForeignKey("pais.id"), nullable=False)
    pais:Mapped["PAIS"] = relationship("PAIS", back_populates="direccion", cascade="all, refresh-expire")
    pedidos:Mapped["PEDIDO"] = relationship("PEDIDO", back_populates="direccion", cascade="all, refresh-expire")
    def __repr__(self):
        return f"DIRECCION(id={self.id}, calle={self.calle}, carrera={self.carrera}, numero={self.numero}, indicador={self.indicador}, diagonal={self.diagonal}, pais={self.pais})"


class IMAGEN_PRODUCTO(Base):
    """
    Representa el modelo de la tabla IMAGEN_PRODUCTO
    """
    __tablename__ = 'imagen_producto'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement="auto")
    url:Mapped[str] = mapped_column(String(50), nullable=False)
    producto_imagen:Mapped["PRODUCTOS"] = relationship("PRODUCTOS", back_populates="imagen_producto", cascade="all, refresh-expire")
   
    def __repr__(self):
        return f"IMAGEN_PRODUCTO(id={self.id}, url={self.url}, producto_id={self.producto_id})"

class CATEGORIA(Base):
    """
    Representa el modelo de la tabla CATEGORIA
    """
    __tablename__ = 'categoria'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement="auto")
    nombre:Mapped[str] = mapped_column(String(50), nullable=False)
    det_producto:Mapped["DETALLE_PRODUCTO"] = relationship("DETALLE_PRODUCTO", back_populates="categoria", cascade="all, refresh-expire")
    def __repr__(self):
        return f"CATEGORIA(id={self.id}, nombre={self.nombre})"

class PRODUCTOS(Base):
    """
    Representa el modelo de la tabla PRODUCTOS
    """
    __tablename__ = 'productos'
    id:Mapped[int]=mapped_column(Integer, primary_key=True, autoincrement="auto")
    nombre:Mapped[str]=mapped_column(String(50), nullable=False)
    imagen_id:Mapped[int]=mapped_column(Integer, ForeignKey('imagen_producto.id'))
    imagen_producto:Mapped["IMAGEN_PRODUCTO"] = relationship("IMAGEN_PRODUCTO", back_populates="producto_imagen", cascade="all, refresh-expire")
    detalle_producto:Mapped["DETALLE_PRODUCTO"] = relationship("DETALLE_PRODUCTO", back_populates="productos", cascade="all, refresh-expire")
    det_pedido:Mapped["DET_PEDIDO"] = relationship("DET_PEDIDO", back_populates="producto", cascade="all, refresh-expire")
    def __repr__(self):
        return f"PRODUCTOS(id={self.id}, nombre={self.nombre})"

class DETALLE_PRODUCTO(Base):
    """
    Representa el modelo de la tabla DETALLE_PRODUCTO
    """
    __tablename__ = 'detalle_producto'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement="auto")
    descripcion:Mapped[str] = mapped_column(String(50), nullable=False)
    precio:Mapped[Numeric] = mapped_column(Numeric, nullable=False)
    cantidad:Mapped[int] = mapped_column(Integer, nullable=False)
    categoria_id:Mapped[int] = mapped_column(Integer, ForeignKey("categoria.id"), nullable=False)
    categoria:Mapped["CATEGORIA"] = relationship("CATEGORIA", back_populates="det_producto", cascade="all, refresh-expire")
    producto_id = mapped_column(Integer, ForeignKey('productos.id'))
    productos:Mapped["PRODUCTOS"] = relationship("PRODUCTOS", back_populates="detalle_producto", cascade="all, refresh-expire")

class PEDIDO(Base):
    """
    Representa el modelo de la tabla PEDIDO
    """
    __tablename__ = 'pedido'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement="auto")
    cantidad:Mapped[int] = mapped_column(Integer, nullable=False)
    det_pedido:Mapped["DET_PEDIDO"] = relationship("DET_PEDIDO", back_populates="pedido", cascade="all, refresh-expire")
    factura:Mapped["FACTURA"] = relationship("FACTURA", back_populates="pedido", cascade="all, refresh-expire")
    direccion_id:Mapped[int] = mapped_column(Integer, ForeignKey('direccion.id'), nullable=False)
    direccion:Mapped["DIRECCION"] = relationship("DIRECCION", back_populates="pedidos", cascade="all, refresh-expire")
class DET_PEDIDO(Base):
    """
    Representa el modelo de la tabla DET_PEDIDO
    """
    __tablename__ = 'det_pedido'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement="auto")
    pedido_id:Mapped[int] = mapped_column(Integer, ForeignKey('pedido.id'), nullable=False)
    pedido:Mapped["PEDIDO"] = relationship("PEDIDO", back_populates="det_pedido", cascade="all, refresh-expire")
    producto_id:Mapped[int] = mapped_column(Integer, ForeignKey('productos.id'), nullable=False)
    producto:Mapped["PRODUCTOS"] = relationship("PRODUCTOS", back_populates="det_pedido", cascade="all, refresh-expire")
    fecha_pedido:Mapped[Date] = mapped_column(Date, nullable=False)
    cliente_id:Mapped[int] = mapped_column(Integer, ForeignKey('clientes.cliente_id'), nullable=False)
    cliente:Mapped["CLIENTES"] = relationship("CLIENTES", back_populates="det_pedido", cascade="all, refresh-expire")
class FACTURA(Base):
    """
    Representa el modelo de la tabla FACTURA
    """
    __tablename__ = 'factura'
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement="auto")
    numero_factura:Mapped[int] = mapped_column(Integer, nullable=False,unique=True)
    fecha_factura:Mapped[Date] = mapped_column(Date, nullable=False)
    total:Mapped[Numeric] = mapped_column(Numeric, nullable=False)
    pedido_id:Mapped[int] = mapped_column(Integer, ForeignKey('pedido.id'), nullable=False)
    pedido:Mapped["PEDIDO"] = relationship("PEDIDO", back_populates="factura", cascade="all, refresh-expire")


