from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model', 'price', 'description', 'image', 'year')
    list_filter = ('manufacturer', )
    search_fields = ('model', )

