# from django.contrib import admin
# from .models import Order

# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['customer', 'car', 'quantity', 'total_price', 'created_at', 'is_confirmed']
#     list_filter = ['is_confirmed']

# from django.contrib import admin
# from .models import *


# class ProductInOrderInline(admin.TabularInline):
#     model = ProductInOrder
#     extra = 0


# class StatusAdmin (admin.ModelAdmin):
#     list_display = [field.name for field in Status._meta.fields]

#     class Meta:
#         model = Status

# admin.site.register(Status, StatusAdmin)


# class OrderAdmin (admin.ModelAdmin):
#     list_display = [field.name for field in Order._meta.fields]
#     inlines = [ProductInOrderInline]

#     class Meta:
#         model = Order

# admin.site.register(Order, OrderAdmin)


# class ProductInOrderAdmin (admin.ModelAdmin):
#     list_display = [field.name for field in ProductInOrder._meta.fields]

#     class Meta:
#         model = ProductInOrder

# admin.site.register(ProductInOrder, ProductInOrderAdmin)


# class ProductInBasketAdmin (admin.ModelAdmin):
#     list_display = [field.name for field in ProductInBasket._meta.fields]

#     class Meta:
#         model = ProductInBasket

# admin.site.register(ProductInBasket, ProductInBasketAdmin)


# from django.contrib import admin
# from .models import Order, CarInOrder, ProductInBasket

# class ProductInOrderInline(admin.TabularInline):
#     model = CarInOrder
#     extra = 0

# class ProductInBasketInline(admin.TabularInline):
#     model = ProductInBasket
#     extra = 0

# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'total_price', 'status', 'created', 'updated')
#     list_filter = ('status', 'created', 'updated')
#     search_fields = ('id', 'user__username', 'customer_name', 'customer_email')
#     inlines = [ProductInOrderInline]

# @admin.register(CarInOrder)
# class ProductInOrderAdmin(admin.ModelAdmin):
#     list_display = ('order', 'product', 'nmb', 'price_per_item', 'total_price', 'created', 'updated')
#     list_filter = ('created', 'updated')
#     search_fields = ('order__id', 'product__model')

# admin.site.register(ProductInBasket)


from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'model', 'order_date', 'is_confirmed', 'total_price']  # Замените 'price' на 'total_price'

admin.site.register(Order, OrderAdmin)