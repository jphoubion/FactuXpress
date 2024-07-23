from django import forms
from django.forms import ModelForm, Form
from .models import User, Company, Customer, Item, Invoice, Invoice_line

class company_form(ModelForm):
    class Meta:
        model = Company
        fields = "__all__"

        DEALER_OR_CUSTOMER = (
            ("dealer", "Dealer"),
            ("customer", "Customer"),
        )

        # is_dealer_or_customer = forms.CheckboxSelectMultiple(choices=DEALER_OR_CUSTOMER)

        widgets = {
                'is_dealer_or_customer': forms.CheckboxSelectMultiple(choices=DEALER_OR_CUSTOMER),
        }
