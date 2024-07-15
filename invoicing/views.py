from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .forms import company_form
from .models import Company, Customer, Item, Invoice, Invoice_line

@login_required()
def index(request):
    companies = Company.objects.all()
    customers = Customer.objects.all()
    invoices = Invoice.objects.all()
    invoice_lines = Invoice_line.objects.all()
    return render(request, "invoicing/index.html", {'companies': companies,
                                                    'customers': customers, 'invoices': invoices, 'invoice_lines': invoice_lines})
@login_required()
def display_companies(request):
    companies = Company.objects.all()
    return render(request, "invoicing/display_companies.html", {'companies': companies})

@login_required()
def create_company(request):
    form = company_form()

    return render(request, "invoicing/create_company.html", {'form': form})

@login_required()
def update_company(request, pk):
    return HttpResponse("update company ok !")

@login_required()
def delete_company(request, pk):
    return HttpResponse("delete company ok !")

