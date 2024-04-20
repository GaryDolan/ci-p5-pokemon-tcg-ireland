from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User

# Tuple to control product sale status
STATUS = ((0, "Not On sale"), (1, "On Sale"))

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_display_name(self):
        return self.display_name
    
class CardSet(models.Model):

    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_display_name(self):
        return self.display_name

class Expansion(models.Model):

    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_display_name(self):
        return self.display_name

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    card_set = models.ForeignKey('CardSet', null=True, blank=True, on_delete=models.SET_NULL)
    expansion = models.ForeignKey('Expansion', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    on_sale = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.name

    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    review_rating = models.IntegerField()
    review_text = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s review of {self.product.name}"
    
