from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,SubmitField 
from wtforms.validators import InputRequired, NumberRange
from flask_wtf.file import FileField, FileRequired, FileAllowed

class ClientForm():
    username = StringField(
        "Ingresa nombre:", validators= [ InputRequired(message='nombre requerido')]
        )
    password = StringField(
        "Ingresa password:", validators= [ InputRequired(message='password requerido')]
        )
    email = StringField(
        "Ingresa email:", validators= [ InputRequired(message='email requerido')]
        )
    submit = SubmitField("Guardar")


class EditClientForm(FlaskForm, ClientForm):
    Submit = SubmitField("Actualizar")