from sqlalchemy import Boolean, Column, ForeignKey, DateTime, Integer, String, Text, Float
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Categorias(db.Model):
    """"Categorias de los articulos"""
    __tablename__ = 'categorias'
    id =  Column(Integer, primary_key=True)
    nombre = Column(String(100))
    articulos = relationship("Articulos", cascade="all, delete-orphan", backref="Categorias", lazy='dynamic')
    def __repr__(self):
        return (u'<{sel.__class__.__name__}: {sel.id}>)'.format(self=self))
    
class Articulos(db.Model):
    """Articulos de nuestra tienda"""
    __tablename__ = 'articulos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=True)
    precio = Column(Float,default=0)
    iva = Column(Integer, default=21)
    descripcion = Column(String(255))
    image = Column(String(255))
    stock = Column(Integer,default=0)
    CategoriaId = Column(Integer, ForeignKey('categorias.id'), nullable=False)
    categoria = relationship("Categorias", backref="Articulos")
    def precio_final(self):
        return self.precio+(self.precio*self.iva/100)
    def __repr__(self):
        return (u'<{self.__class__.name__}: {self.id}>'.format(self=self))
    
class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    username = Column(String(100),nullable=False)
    password_hash = Column(String(128),nullable=False)
    nombre = Column(String(200),nullable=False)
    email = Column(String(200),nullable=False)
    admin = Column(Boolean, default=False)
    def __repr(self):
        return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))
    @property
    def password(self):
        raise AttributeError('passwor is not a readable atribute')
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    def verify_password(self, password):
        return check_password_hash(self.password, password)
