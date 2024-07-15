from django.shortcuts import render
from .forms import company_form
from .models import Company, Customer, Item, Invoice, Invoice_line


def index(request):
    companies = Company.objects.all()
    customers = Customer.objects.all()
    invoices = Invoice.objects.all()
    invoice_lines = Invoice_line.objects.all()
    form = company_form()
    return render(request, "invoicing/index.html", {'form': form, 'companies': companies,
                                                    'customers': customers, 'invoices': invoices, 'invoice_lines': invoice_lines})

def display_companies(request):
    companies = Company.objects.all()
    return render(request, "invoicing/display_companies.html", {'companies': companies})

