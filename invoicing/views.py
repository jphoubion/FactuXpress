from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
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
    context = {'companies': companies}
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
    context = {'customers': customers}
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
    return render(request, "invoicing/display_items.html", {'items': items})

@login_required()
def create_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("invoicing:items")
        else:
            form = ItemForm(request.POST)
            return render(request, "invoicing/create_item.html", {"form": form})
    else:
        form = ItemForm()
        return render(request, "invoicing/create_item.html", {"form": form})

@login_required()
def update_item(request,pk):
    pass

@login_required()
def deactivate_item(request,pk):
    pass

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
