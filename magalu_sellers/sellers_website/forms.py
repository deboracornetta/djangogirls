from django import forms

class List_Form(forms.Form):
    text = forms.CharField(max_length=100,
    widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Insira um produto'
        }
     ))