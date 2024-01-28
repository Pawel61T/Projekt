from django.db import models
from users.models import User
from django_countries.fields import CountryField
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Offer(models.Model):
    OFFER_TYPE = (
        ("1", "Room"),
        ("2", "Local"),
    )

    offer_type = models.CharField(choices =OFFER_TYPE, max_length = 15, default = "Room")
    price = models.IntegerField(default = None, validators = [MinValueValidator(0)])
    size = models.FloatField(default = None, validators = [MinValueValidator(0)])
    #room field
    capacity = models.IntegerField(blank=True, null = True, validators = [MinValueValidator(0)])
    #local field
    number_of_rooms = models.IntegerField(blank=True, null = True, validators = [MinValueValidator(0)])
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField(max_length=10000, blank=True)
    address1 = models.CharField("Address line 1", max_length=1024,)
    address2 = models.CharField("Address line 2", max_length=1024, blank=True)
    zip_code = models.CharField("ZIP / Postal code", max_length=12,)
    city = models.CharField("City", max_length=1024,)
    country = CountryField(blank_label="(select country)")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    REQUIRED_FIELDS = ['price', 'size']