
from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'date_created', 'car')
    list_filter = ('date_created', )
    search_fields = ('customer__username', )  # Пример поиска по имени пользователя

admin.site.register(Order, OrderAdmin)
