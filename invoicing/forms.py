from django import forms
from django.forms import ModelForm, Form
from .models import User, Company, Customer, Item, Unity_of_measure, Invoice, Invoice_line


class CompanyForm(ModelForm):
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


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = "__all__"


class UnitiesOfMeasureForm(ModelForm):
    class Meta:
        model = Unity_of_measure
        fields = "__all__"


class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = "__all__"


class InvoiceLineForm(ModelForm):
    class Meta:
        model = Invoice_line
        fields = "__all__"
