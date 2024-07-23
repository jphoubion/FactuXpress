from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import company_form
from .models import Company, Customer, Item, Invoice, Invoice_line
from django.utils.translation import gettext_lazy as _

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
    context = {'companies': companies}
    return render(request, "invoicing/display_companies.html", context)

@login_required()
def create_company(request):
    if request.method == "POST":
        form = company_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("invoicing:companies")
        else:
            form = company_form(request.POST)
            return render(request, "invoicing/create_company.html", {'form': form})
    else:
        form = company_form()
        return render(request, "invoicing/create_company.html", {'form': form})

@login_required()
def update_company(request,pk):
    print(pk)
    if pk == 0:
        print(request.GET.get('company_id'))
        company = Company.objects.get(pk=request.GET.get('company_id'))
    else:
        company = Company.objects.get(pk=pk)

    if request.method == "GET":
        form = company_form(instance=company)
        return render(request, "invoicing/update_company.html", {'form': form, 'company': company})
    else:
        form = company_form(request.POST,instance=company)
        if form.is_valid():
            form.save()
            return redirect("invoicing:index")
        return render(request, "invoicing/update_company.html", {'form': form, 'company': company})

@login_required()
def deactivate_company(request, pk):
    if pk == 0:
        print(request.GET.get('company_id'))
        company = Company.objects.get(pk=request.GET.get('company_id'))
    else:
        company = Company.objects.get(pk=pk)

    return HttpResponse("delete company ok !")

