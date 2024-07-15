from django.urls import path
from invoicing import views

app_name = "invoicing"

urlpatterns = [
    path("", views.index, name='index'),
    path("companies", views.display_companies, name="companies"),
]