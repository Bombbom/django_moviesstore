from django.contrib import admin
from .models import Order , Item 
# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass
    