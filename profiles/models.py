from django.db import models
from django.contrib.auth.models import User

from django_countries.fields import CountryField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    default_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_city = models.CharField(max_length=45, null=True, blank=True)
    default_zipcode = models.CharField(max_length=25, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)
    default_phone = models.CharField(max_length=20, null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True)
    avatar_url = models.URLField(null=True, blank=True)
    # reviews = models.ForeignKey()
    store_name = models.CharField(max_length=100, null=True, blank=True)
    seller_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    verified = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.user.username
    
    # Placeholder for seller payment handling functions
