from django.urls import path
from invoicing import views

app_name = "invoicing"

urlpatterns = [
    path("", views.index, name='index'),

    path("companies", views.display_companies, name="companies"),
    path("create_company", views.create_company, name="create-company"),
    path("update_company/<int:pk>", views.update_company, name="update-company"),
    path("deactivate_company/<int:pk>/", views.deactivate_company, name="deactivate-company"),
    path("invoice_from_company/<int:pk>", views.invoice_from_company, name="invoice-from-company"),
    path("print_company/<int:pk>", views.print_company, name="print-company"),

    path("customers", views.display_customers, name="customers"),
    path("create_customer", views.create_customer, name="create-customer"),
    path("update_customer/<int:pk>", views.update_customer, name="update-customer"),
    path("deactivate_customer/<int:pk>/", views.deactivate_customer, name="deactivate-customer"),
    path("invoice_from_customer/<int:pk>", views.invoice_from_customer, name="invoice-from-customer"),
    path("print_customer/<int:pk>", views.print_customer, name="print-customer"),

    path("items", views.display_items, name="items"),
    path("items/<str:item_type>", views.display_items_filtered, name="display-items-filtered"),
    path("create_item", views.create_item, name="create-item"),
    path("update_item/<int:pk>", views.update_item, name="update-item"),
    path("print_item/<int:pk>", views.print_item, name="print-item"),
]
