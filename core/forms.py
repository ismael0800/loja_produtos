from django import forms
from .models import Cliente, Venda

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = '__all__'
