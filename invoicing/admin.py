from django.contrib import admin
from .models import User, Company, Customer, Item, Invoice, Invoice_line, Unity_of_measure


admin.site.register(User)
admin.site.register(Company)
admin.site.register(Customer)
admin.site.register(Item)
admin.site.register(Invoice)
admin.site.register(Invoice_line)
admin.site.register(Unity_of_measure)
