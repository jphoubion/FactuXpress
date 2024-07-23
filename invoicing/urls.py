from django.urls import path
from invoicing import views

app_name = "invoicing"

urlpatterns = [
    path("", views.index, name='index'),
    path("companies", views.display_companies, name="companies"),
    path("create_company", views.create_company, name="create-company"),
    path("update_company/<int:pk>", views.update_company, name="update-company"),
    path("deactivate_company/<int:pk>/", views.deactivate_company, name="deactivate-company"),
]
