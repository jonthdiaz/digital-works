# -*- coding: utf-8 -*-
from django import forms
from .models import Contact
from django.forms import ValidationError


class ContactForm(forms.ModelForm):
    """
        Formulario de contactanos
    """
    class Meta:
        model = Contact
        fields = ['name', 'email', 'observations']

    def clean(self):
        name = self.cleaned_data.get("name")
        email = self.cleaned_data.get("email")
        observations = self.cleaned_data.get("observations")

        if not name:
            raise ValidationError(message=u"El nombre es requerido")
        if not email:
            raise ValidationError(message=u"El email es requerido")
        if not observations:
            raise ValidationError(message=u"Las observaciones son requeridas")

        return self.cleaned_data
