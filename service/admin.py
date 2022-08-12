from django.contrib import admin

# Register your models here.
from service.models import Product, Bin, Home

admin.site.register(Bin)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'cost', 'is_active']
    list_filter = ['cost']
    search_fields = ['title']


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['id', 'cost', 'size', 'adr', 'bal']
