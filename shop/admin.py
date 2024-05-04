from django.contrib import admin

from . models import Product, Contact, Orders, orderUpdate, Shopdetail


# Register your models here.


class orderview(admin.ModelAdmin):
    list_display = ['order_id', 'item_json', 'name']


class productview(admin.ModelAdmin):
    list_display = ['product_name', 'category', 'pub_date', 'shop_id']


class shopview(admin.ModelAdmin):
    list_display = ['shop_id', 'shop_name', 'shop_email']


admin.site.register(Product, productview)
admin.site.register(Contact)
admin.site.register(Orders,orderview)
admin.site.register(orderUpdate)
admin.site.register(Shopdetail, shopview)
