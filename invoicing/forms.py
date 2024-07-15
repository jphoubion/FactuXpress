from django import forms
from django.forms import ModelForm, Form
from .models import User, Company, Customer, Item, Invoice, Invoice_line

class company_form(ModelForm):
    class Meta:
        model = Company
        fields = "__all__"

        widgets = {
            'is_dealer_or_customer': forms.CheckboxSelectMultiple(),
        }
