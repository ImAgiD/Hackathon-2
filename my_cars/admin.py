from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model', 'price', 'description', 'image', 'year')
    list_filter = ('manufacturer', )
    search_fields = ('model', )

# admin.site.register(Car, CarAdmin)

# from django.contrib import admin


# from .models import Car, Client
 

# @admin.register(Car)
# class PersonAdmin(admin.ModelAdmin):
#     list_display = ('марка', 'производитель', 'цена', 'описание')
#     search_fields = ('марка', 'производитель', 'цена', 'описание')
#     list_filter = ('марка', 'производитель', 'цена', 'описание')
#     list_per_page = 50


# @admin.register(Client)
# class ClientAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'phone', 'address')
#     search_fields = ('name', 'email', 'phone', 'address')
#     list_per_page = 50
