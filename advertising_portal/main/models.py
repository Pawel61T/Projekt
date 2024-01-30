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


class Opinion(models.Model):
    comment = models.TextField(max_length=200)
    rating = models.IntegerField(default = 5, validators = [MinValueValidator(1), MaxValueValidator(5)])
    date = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    offert = models.ForeignKey(Offer, on_delete=models.CASCADE)

class Reservation(models.Model):
    check_in = models.DateField(auto_now=False, auto_now_add=False)
    check_out = models.DateField(auto_now=False, auto_now_add=False)
    arrival_hour = models.TimeField()
    offert = models.ForeignKey(Offer, on_delete = models.CASCADE, default = None)
    guest = models.ForeignKey(User, on_delete= models.CASCADE)
    is_waiting = models.BooleanField(default=True)
    is_accepted = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['check_in', 'check_out', 'arrival_hour']