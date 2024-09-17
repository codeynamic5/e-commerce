from django.contrib import admin
# Register your models here.
from .models import ProductEntry

class ProductAdmin(admin.ModelAdmin):
  list_display = ('name', 'price', 'image', 'description')

admin.site.register(ProductEntry, ProductAdmin)