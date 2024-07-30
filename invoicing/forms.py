import logging

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

        widgets = {
                'is_dealer_or_customer': forms.CheckboxSelectMultiple(choices=DEALER_OR_CUSTOMER),
        }


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class ItemForm(ModelForm):
    # Init block required to filter the ITEMS to avoid having "group_item" in the
    # def __init__(self, key, *args, **kwargs):
    #     super(ItemForm, self).__init__(*args, **kwargs)
    #     self.fields['group_item_child_item'].queryset = (
    #         self.fields['group_item_child_item'].queryset.exclude(is_a_group_item=True)).order_by("fastcode")

    class Meta:
        model = Item
        fields = "__all__"

        group_item_child_item = forms.MultipleChoiceField()

        widgets = {
                'description': forms.Textarea(attrs={'rows': 4}),
                'remark': forms.Textarea(attrs={'rows': 4}),
                'group_item_child_item': forms.SelectMultiple(attrs={'size': 10, 'class': "w-full"})
        }

    def clean(self):
        cleaned_data = super().clean()
        is_a_group_item = cleaned_data['is_a_group_item']
        group_item_child_item = cleaned_data['group_item_child_item']
        if is_a_group_item and not group_item_child_item:
            self.add_error("group_item_child_item", "Sélectionnez les articles qui composent l'article groupé !")


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
