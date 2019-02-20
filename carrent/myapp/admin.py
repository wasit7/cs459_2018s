from django.contrib import admin
from .models import Customer, Car, Rent

class CustomerAdmin(admin.ModelAdmin):
    fields = ('firstname', 'lastname', 'dob', 'tel')
    list_display = ('firstname', 'lastname', 'dob', 'tel')
    list_filter = ('dob', )
    list_editable = ('tel', )

admin.site.register(Customer, CustomerAdmin)

class CarAdmin(admin.ModelAdmin):
    fields = ('brand','price','purchasing_date')
    list_display = ('brand','price','purchasing_date')
    list_filter = ('brand','purchasing_date')

admin.site.register(Car, CarAdmin)

class RentAdmin(admin.ModelAdmin):
    fields = ('start','stop','cost','car','customer')
    list_display = ('start','stop','cost','car','customer')

admin.site.register(Rent, RentAdmin)
