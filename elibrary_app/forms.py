from django import forms
from .models import Catalog


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = "__all__"

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'ISBN': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'availability': forms.Select(attrs={
                'class': 'form-control'
            })
        }
