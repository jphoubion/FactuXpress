import logging

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .forms import CompanyForm, CustomerForm, ItemForm, UnitiesOfMeasureForm, InvoiceForm, InvoiceLineForm
from .models import Company, Customer, Item, Unity_of_measure, Invoice, Invoice_line


@login_required()
def index(request):
    companies = Company.objects.all()
    customers = Customer.objects.all()
    quotations = Invoice.objects.filter(status="quotation").order_by("reference")
    orders = Invoice.objects.filter(status="order").order_by("reference")
    invoices = Invoice.objects.filter(status="invoice").order_by("reference")
    return render(request, "invoicing/index.html", {'companies': companies,
                                                    'customers': customers,'quotations':quotations, 'orders':orders,
                                                    'invoices': invoices})

####################################
# COMPANIES
####################################


@login_required()
def display_companies(request):
    companies = Company.objects.all()

    paginator = Paginator(companies, 10)  # Show 10 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {'companies': companies, "page_obj": page_obj}
    return render(request, "invoicing/display_companies.html", context)

@login_required()
def display_companies_filtered(request, company_type):
    match company_type:
        case "all":
            companies = Company.objects.all()
        case "active":
            companies = Company.objects.filter(is_active=True)
        case "inactive":
            companies = Company.objects.filter(is_active=False)

    paginator = Paginator(companies, 10)  # Show 10 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'companies': companies, 'company_type': company_type, "page_obj": page_obj}

    return render(request, "invoicing/display_companies.html", context)

@login_required()
def create_company(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("invoicing:companies")
        else:
            form = CompanyForm(request.POST)
            return render(request, "invoicing/create_company.html", {'form': form})
    else:
        form = CompanyForm()
        return render(request, "invoicing/create_company.html", {'form': form})


@login_required()
def update_company(request,pk):
    company = Company.objects.get(pk=pk)

    if request.method == "GET":
        form = CompanyForm(instance=company)
        return render(request, "invoicing/update_company.html", {'form': form, 'company': company})
    else:
        form = CompanyForm(request.POST,instance=company)
        if form.is_valid():
            form.save()
            return redirect("invoicing:companies")
        return render(request, "invoicing/update_company.html", {'form': form, 'company': company})


@login_required()
def deactivate_company(request, pk):
    company = Company.objects.get(pk=pk)

    if company.is_active:
        company.is_active = False
    else:
        company.is_active = True

    company.save(update_fields=['is_active'])
    return redirect("invoicing:companies")


def invoice_from_company(request,pk):
    return HttpResponse("Facturer depuis la société !")


def print_company(request,pk):
    return HttpResponse('Impression de la société !')

##############################################
# CUSTOMERS
##############################################

@login_required()
def display_customers(request):
    customers = Customer.objects.all()

    paginator = Paginator(customers, 10)  # Show 10 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {'customers': customers, "page_obj": page_obj}

    return render(request, "invoicing/display_customers.html", context)

@login_required()
def display_customers_filtered(request, customer_type):
    match customer_type:
        case "all":
            customers = Customer.objects.all()
        case "active":
            customers = Customer.objects.filter(is_active=True)
        case "inactive":
            customers = Customer.objects.filter(is_active=False)

    paginator = Paginator(customers, 10)  # Show 10 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {'customers': customers, 'customer_type': customer_type, "page_obj": page_obj}

    return render(request, "invoicing/display_customers.html", context)


@login_required()
def create_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("invoicing:customers")
        else:
            form = CustomerForm(request.POST)
            return render(request, "invoicing/create_customer.html", {'form': form})
    else:
        form = CustomerForm()
        return render(request, "invoicing/create_customer.html", {'form': form})


@login_required()
def update_customer(request,pk):

    customer = Customer.objects.get(pk=pk)

    if request.method == "GET":
        form = CustomerForm(instance=customer)
        return render(request, "invoicing/update_customer.html", {'form': form, 'customer': customer})
    else:
        form = CustomerForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect("invoicing:customers")
        return render(request, "invoicing/update_customer.html", {'form': form, 'customer': customer})


@login_required()
def deactivate_customer(request, pk):

    customer = Customer.objects.get(pk=pk)

    if customer.is_active:
        customer.is_active = False
    else:
        customer.is_active = True

    customer.save(update_fields=['is_active'])
    return redirect("invoicing:customers")


@login_required()
def invoice_from_customer(request,pk):
    return HttpResponse("Facturer depuis le client !")


@login_required()
def print_customer(request,pk):
    return HttpResponse('Impression du client !')


##############################################
# ITEMS
##############################################

@login_required()
def display_items(request):
    items = Item.objects.all()

    paginator = Paginator(items, 10)  # Show 10 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {'items': items, "page_obj": page_obj}
    return render(request, "invoicing/display_items.html", context)

@login_required()
def display_items_filtered(request, item_type):
    match item_type:
        case "all":
            items = Item.objects.all()
        case "grouped":
            items = Item.objects.filter(is_a_group_item=True)
        case "normal":
            items = Item.objects.filter(is_a_group_item=False)

    paginator = Paginator(items, 10)  # Show 10 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {'items': items, 'item_type':item_type, "page_obj": page_obj}

    return render(request, "invoicing/display_items.html", context)


@login_required()
def create_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        print(request.POST)
        print(form.is_valid())
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.save()
            form.save_m2m()
            return redirect("invoicing:items")
        else:
            form = ItemForm(request.POST)
            return render(request, "invoicing/create_item.html", {"form": form})
    else:
        # form = ItemForm(key='group_item_child_item')
        form = ItemForm()
        return render(request, "invoicing/create_item.html", {"form": form})

@login_required()
def update_item(request,pk):

    item = Item.objects.get(pk=pk)

    if request.method == "GET":
        form = ItemForm(instance=item)
        return render(request, "invoicing/update_item.html", {'form': form, 'item': item})
    else:
        form = ItemForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect("invoicing:items")
        return render(request, "invoicing/update_item.html", {'form': form, 'item': item})


@login_required()
def print_item(request,pk):
    pass

##############################################
# INVOICES
##############################################

@login_required()
def create_commercial_document(request):
    form = None
    return render(request, "invoicing/create_commercial_document.html", {'form': form})

def update_commercial_document(request,pk):
    pass

def reject_quotation(request,pk):
    pass

def quotation_to_order(request,pk):
    pass

def order_to_invoice(request,pk):
    pass

def print_commercial_document(request,pk):
    pass
