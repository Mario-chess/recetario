#encoding:utf-8 
from django.forms import ModelForm

from django import forms

from principal.models import *

from django.contrib.auth.models import User

# from ckeditor.widgets import CKEditor

from ckeditor.widgets import CKEditorWidget


class ContactoForm(forms.Form):
	correo = forms.EmailField(label='Tu correo electrónico')
	mensaje = forms.CharField(widget=forms.Textarea)


class RecetaForm(ModelForm):
    class Meta:
        model = Receta


class ComentarioForm(ModelForm):
	texto = forms.CharField(widget=CKEditorWidget())
	class Meta:
		model = Comentario


# Primero sera necesario ampliar el modelo User en models.py
# Luego habra que llamar a dicho modelo y hacerlo Formulario
# Cargarlo en una plantilla

class UserForm(ModelForm):
	password = forms.CharField(label="Password", widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ('username', 'email', 'password', 'imagen') 

	