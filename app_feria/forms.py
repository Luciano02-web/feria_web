from distutils.command.upload import upload
from tkinter import CASCADE
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import User

from app_feria.models import Imagen
"""
from app_feria.models import Avatar, Imagen"""










"""
class FormuJean(forms.Form):
    id_vuelo = forms.IntegerField()
    salida = forms.CharField(max_length=50)
    destino = forms.CharField(max_length=50)
    fecha = forms.DateField()    #2022-05-23(AAAA-MM-DD)
    hora_de_salida = forms.TimeField() #02:13(HH:MM)




    <table align="center">
        <p>
            <div>
                <h4>Ingrese datos del jean</h4>
                {{formulario1.as_table}}
            </div>
        </p>
    </table>

class FormuJean(forms.Form):
    imagen = forms.ImageField()#blank=True
    codigo = forms.IntegerField()
    talle = forms.IntegerField()
    color = forms.CharField(max_length=50)
    precio = forms.IntegerField()
    class Meta:

        model = Imagen
        fields = ["imagen"]
"""


class FormuJean(forms.Form):
    imagen = forms.ImageField(required=False)
    codigo = forms.IntegerField(required=False)
    talle = forms.CharField(max_length=50, required=False)
    color = forms.CharField(max_length=50, required=False)
    genero = forms.CharField(max_length=50, required=False)
    precio = forms.IntegerField(required=False)
    class Meta:

        model = Imagen
        fields = ["imagen"]

class FormuRemera(forms.Form):
    imagen = forms.ImageField(required=False)#blank=True
    codigo = forms.IntegerField(required=False)
    talle = forms.CharField(max_length=50, required=False)
    color = forms.CharField(max_length=50, required=False)
    genero = forms.CharField(max_length=50, required=False)
    precio = forms.IntegerField(required=False)
    class Meta:

        model = Imagen
        fields = ["imagen"]


class FormuCamisa(forms.Form):
    imagen = forms.ImageField(required=False)
    codigo = forms.IntegerField(required=False)
    talle = forms.CharField(max_length=50, required=False)
    color = forms.CharField(max_length=50, required=False)
    genero = forms.CharField(max_length=50, required=False)
    precio = forms.IntegerField(required=False)
    class Meta:

        model = Imagen
        fields = ["imagen"]

class FormuCampera(forms.Form):
    imagen = forms.ImageField(required=False)
    codigo = forms.IntegerField(required=False)
    talle = forms.CharField(max_length=50, required=False)
    color = forms.CharField(max_length=50, required=False)
    genero = forms.CharField(max_length=50, required=False)
    precio = forms.IntegerField(required=False)
    class Meta:

        model = Imagen
        fields = ["imagen"]

class FormuTodo100(forms.Form):
    imagen = forms.ImageField(required=False)
    codigo = forms.IntegerField(required=False)
    talle = forms.CharField(max_length=50, required=False)
    color = forms.CharField(max_length=50, required=False)
    genero = forms.CharField(max_length=50, required=False)
    precio = forms.IntegerField(required=False)
    class Meta:

        model = Imagen
        fields = ["imagen"]

class FormuCalzado(forms.Form):
    imagen = forms.ImageField(required=False)
    codigo = forms.IntegerField(required=False)
    talle = forms.CharField(max_length=50, required=False)
    color = forms.CharField(max_length=50, required=False)
    genero = forms.CharField(max_length=50, required=False)
    precio = forms.IntegerField(required=False)
    class Meta:

        model = Imagen
        fields = ["imagen"]
"""
class FormuPasajero(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    documento = forms.IntegerField()
    id_vuelo = forms.IntegerField()
"""

class FormularioRegistro(UserCreationForm):
    email = forms.EmailField(label='Ingrese email')
    first_name= forms.CharField(label='Ingrese nombre')
    last_name= forms.CharField(label='Ingrese apellido')
    password1 = forms.CharField(label='Ingrese la contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["username","first_name","last_name","email","password1","password2"]

class FormularioEditarUsuario(UserCreationForm):
    email = forms.EmailField(label='Ingrese email')
    first_name= forms.CharField(label='Ingrese nombre')
    last_name= forms.CharField(label='Ingrese apellido')
    password1 = forms.CharField(label='Ingrese la contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["first_name","last_name","email","password1","password2"]
"""
class FormuAvatar(forms.ModelForm):

    class Meta:

        model = Avatar
        fields = ["imagen"]
"""