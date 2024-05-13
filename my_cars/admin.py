from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'manufacturer', 'model', 'price', 'description', 'year')
    list_filter = ('manufacturer', )
    search_fields = ('model', )
