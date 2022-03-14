from socket import fromshare
from django import forms 
from user.models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"