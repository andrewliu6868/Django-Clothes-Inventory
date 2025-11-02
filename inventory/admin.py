from django.contrib import admin
from .models import CategoryModel, TagModel, ProductModel
# Register your models here.

admin.site.register(CategoryModel)
admin.site.register(TagModel)
admin.site.register(ProductModel)