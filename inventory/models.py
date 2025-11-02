from django.db import models
from django.urls import reverse

class CategoryModel(models.Model):
    # category field
    name = models.CharField(max_length=100, help_text='Enter category name', unique=True)
    
    # category metadata
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=["name"])
        ]
        
    # methods necessary for Django
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("category-details", args=[str(self.id)])
    

class TagModel(models.Model):
    # tag field
    name = models.CharField(max_length=100, help_text='Enter tag name', unique=True)
    
    # tag metadata
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=["name"])
        ]
        
    # methods necessary for Django
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("tag-details", args=[str(self.id)])
    
    
class ProductModel(models.Model):
    # product fields
    name = models.CharField(max_length=100, help_text='Enter product name', unique=True)
    description = models.TextField(max_length=200, blank=True)
    category = models.ForeignKey( CategoryModel, on_delete=models.PROTECT, related_name="products", null=True, blank=True) # one category per product
    tags = models.ManyToManyField(TagModel, related_name="products", blank=True) # allow many tags per product
    
    # product meta data
    class Meta:
        ordering = ['name', 'category'] # order by name first then category (alphabetical)
        indexes = [
            models.Index(fields=["name"])
        ]
        
    # methods necessary for Django
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("product-details", args=[str(self.id)])
    