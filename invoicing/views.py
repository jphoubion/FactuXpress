from django.shortcuts import render
from .forms import company_form

def index(request):
    form = company_form()
    return render(request, "invoicing/index.html", {'form':form})
