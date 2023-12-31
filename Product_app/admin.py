from django.contrib import admin
from .models import Category, ProductType, Brand, Product, Warranty

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug']
    prepopulated_fields = {'slug': ('category_name', )}
    ordering = ['id']
   
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug']
    prepopulated_fields = {'slug': ('product_type', )}
    ordering = ['id']
    
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug']
    prepopulated_fields = {'slug': ('brand_name', )}
    ordering = ['id']
    
class WarrantyAdmin(admin.ModelAdmin):
    list_display = ['id', 'slug']
    prepopulated_fields = {'slug': ('warranty_duration', )}
    ordering = ['id']
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'image', 'slug', 'category', 'warranty', 'product_type', 'brand', 'price',
                    'product_title']
    prepopulated_fields = {'slug': ('product_name', )}
    ordering = ['id']
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Warranty, WarrantyAdmin)
admin.site.register(Product, ProductAdmin)