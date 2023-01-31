from django.contrib import admin
from . import models
# Register your models here.
admin.site.site_header = "SSF Administartion"
admin.site.site_title = "SSF Administration"
admin.site.index_title = ""


# class Categoryadmin(admin.ModelAdmin):
# 	date_hierarchy = 'created_at'
# 	search_fields = ['name']
# 	list_display = ('name', 'description')
# 	list_filter = ('created_at',)


# class ProductAdmin(admin.ModelAdmin):
# 	date_hierarchy = 'created_at'
# 	search_fields = ['name']
# 	list_display = ('name', 'price', 'stock', 'category', 'description')
# 	list_filter = ('created_at', 'category',)
# 	actions = ['make_price_zero','make_price_discount_20']


# 	def make_price_zero(modelsadmin, request, queryset):
# 		queryset.update(price=0)
# 	make_price_zero.short_description = "Make selected product free"

# 	def make_price_discount_20(modelsadmin, request, queryset):
# 		for product in queryset:
# 			result = product.price * 80 / 100
# 			queryset.update(price=result)
# 	make_price_discount_20.short_description = "Make price discount 20"

# admin.site.register(models.Product, ProductAdmin)
# admin.site.register(models.Category, Categoryadmin)
# admin.site.register(models.User)
admin.site.register(models.Portfolio)
admin.site.register(models.Collection)
admin.site.register(models.Invesment)

