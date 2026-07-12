from django.contrib import admin
from .models import Shop, Category, Product, Order

class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'village', 'address')
    search_fields = ('name', 'village')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    filter_horizontal = ('shops',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'delivery_schedule')
    search_fields = ('name',)
    list_filter = ('category',)
    filter_horizontal = ('shops',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'shop', 'product_request', 'created_at')
    search_fields = ('customer_name', 'phone')
    list_filter = ('shop', 'created_at')

admin.site.register(Shop, ShopAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)