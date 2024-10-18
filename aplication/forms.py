from flask_wtf import FlaskForm
from wtforms import DecimalField, IntegerField, SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class formArticulo(FlaskForm):
    nombre=StringField("Nombre:",validators=[DataRequired("Tienes que introducir el dato")])
    precio=DecimalField("Precio:",default=0,validators=[DataRequired("Tienes que introducir el dato")])
    iva=IntegerField("IVA:",default=21,validators=[DataRequired("Tienes que introducir el dato")])
    descripcion= TextAreaField("Descripción:")
    photo = FileField("Selecciona imagen:")
    stock=IntegerField("Stock",default=1,validators=[DataRequired("Tienes que introducir el dato")])
    CategoriaId=SelectField("Categoría:", coerce=int)
    submit = SubmitField('Enviar')
class formCategoria(FlaskForm):
    nombre=StringField("Nombre:",validators=[DataRequired("Tienes que introducir el dato")])
    submit = SubmitField('Enviar')
class formSINO(FlaskForm):
    si = SubmitField('Si')
    no = SubmitField('No')

class LoginForm(FlaskForm):
    username = StringField('Login', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Entrar')