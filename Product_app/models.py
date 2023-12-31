from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug          = models.SlugField(max_length= 200, unique=True)
    description   = models.TextField()
    cate_img      = models.ImageField(upload_to='photos/category', blank=True)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['id']
        
    def __str__(self) -> str:
        return self.category_name


class Warranty(models.Model):
    warranty_duration = models.CharField(max_length=50, default='No Warranty')
    slug              = models.SlugField(max_length= 200, blank=True)
    description   = models.TextField()
    
    class Meta:
        verbose_name = 'Warranty'
        verbose_name_plural = 'Warrants'
        ordering = ['id']
        
    def __str__(self) -> str:
        return self.warranty_duration
    
class ProductType(models.Model):
    product_type = models.CharField(max_length=50, unique=True)
    slug         = models.SlugField(max_length=200, blank=True)
    description   = models.TextField()
    
    class Meta:
        verbose_name = 'Product Type'
        verbose_name_plural = 'Product Types'
        ordering = ['id']
        
    def __str__(self) -> str:
        return self.product_type
        
        
    
class Brand(models.Model):
    brand_name = models.CharField(max_length=150, unique=True)
    slug       = models.SlugField(max_length= 200, blank=True)
    description   = models.TextField()
    
    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        ordering = ['id']
        
    def __str__(self) -> str:
        return self.brand_name


class Product(models.Model):
    category      = models.ForeignKey(Category, on_delete= models.CASCADE, related_name='category')
    warranty      = models.ForeignKey(Warranty, on_delete=models.CASCADE, related_name= 'warranty')
    product_type  = models.ForeignKey(ProductType, on_delete= models.CASCADE, related_name='product_types')
    brand         = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand')
    product_name  = models.CharField(max_length= 50)
    product_title = models.CharField(max_length= 200)
    price         = models.IntegerField()
    image         = models.ImageField(upload_to= 'photos/product', blank=True)
    stock         = models.IntegerField()
    is_available  = models.BooleanField(default= True)
    created_date  = models.DateTimeField(auto_now_add=True)
    modify_date   = models.DateTimeField(auto_now=True)
    slug          = models.SlugField(max_length= 200, unique=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['id']
        
    def __str__(self) -> str:
        return self.product_name



