from django.contrib import admin
from catalog.models import Product, Category, Version


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'category', 'purchase_price',)
#     list_filter = ('category',)
#     search_fields = ('name', 'description',)
#
#
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'name', 'description', 'product', )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'purchase_price',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description',)


@admin.register(Category)
class CategoryAdmin(CategoryAdmin):
    pass


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('version_title', 'version_number', 'sign_current_version',)
    list_filter = ('version_title',)
