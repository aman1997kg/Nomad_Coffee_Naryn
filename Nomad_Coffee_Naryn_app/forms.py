from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['full_name', 'email', 'phone_number', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'tm-form-control', 'placeholder': 'Ф.И.О'}),
            'email': forms.EmailInput(attrs={'class': 'tm-form-control', 'placeholder': 'Email'}),
            'phone_number': forms.NumberInput(attrs={'class': 'tm-form-control', 'placeholder': 'Телефон'}),
            'message': forms.Textarea(attrs={'class': 'tm-form-control', 'placeholder': 'Сообщения'}),
        }