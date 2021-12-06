import random
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User

from profiles.models import UserProfile


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    category_order = models.IntegerField(default=0)

    class Meta:
        ordering = ['category_order']
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.category_name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    sku = models.CharField(max_length=20, null=False, editable=False)
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="product/", null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to="product/thumbnails/", null=True, blank=True)
    thumbnail_url = models.URLField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
        verbose_name_plural = 'Products'
    
    # Over-ride default save function to set slug field
    def save(self, *args, **kwargs):
        self.sku = random.randrange(10**1, 10**20)
        slug_name = str(self.seller) + str(self.product_name)
        self.slug = slugify(slug_name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.product_name

    # Placeholder for function to get thumbnail, or make thumbnail from uploaded image


    # Placeholder for make thumbnail helper function

    # Generate url for products to be used in front-end navigation
    def get_absolute_url(self):
        return reverse("product:product_detail", kwargs={
            'slug': self.slug,
            })

    # Add product to cart url helper function
    def get_add_to_cart_url(self):
        return reverse("cart:add_to_cart", kwargs={
            'slug': self.slug,
            })

    # Remove product from cart url helper function
    def get_remove_from_cart_url(self):
        return reverse("cart:remove_from_cart", kwargs={
            'slug': self.slug,
            })


class Review(models.Model):
    title = models.CharField(max_length=100)
    body_content = models.TextField()
    added_by = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField()
    product_reviewed = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-added_on']
        verbose_name_plural = 'Reviews'
    
    def __str__(self):
        return self.title
