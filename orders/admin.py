from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["size", "order_status", "quantity"]
    list_filter = ["size", "order_status", "created_at"]