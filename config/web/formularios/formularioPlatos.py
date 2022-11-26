
from django import forms

class FormularioPlatos(forms.Form):

    PLATOS = (
            (1, 'Entrada'),
            (2, 'Plato fuerte'),
            (3, 'Bebida'),
            (4, 'Postre'),
    )
    nombre = forms.CharField(
            required=True,
            max_length=20,
            widget=forms.TextInput(attrs={'class': 'form-control mb-3'})
    )

    descripcion = forms.CharField(
            required=True,
            max_length=500,
            widget=forms.Textarea(attrs={'class': 'form-control mb-3'})
    )

    fotografia = forms.CharField(
            required=True,
            widget=forms.Textarea(attrs={'class': 'form-control mb-3'})

    )
    precio= forms.CharField(
            required=True,
            max_length=20,
            widget=forms.NumberInput(attrs={'class': 'form-control mb-3'}) 
    )
    tipo= forms.ChoiceField(
            required=True,      
            widget=forms.Select(attrs={'class': 'form-control mb-3'}),
            choices=PLATOS
    )
