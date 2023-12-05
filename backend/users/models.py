from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password = None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password = None, **extra_fields):
        user = self.create_user(
            email, password, **extra_fields)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class User(AbstractUser):
    username = None
    email = models.EmailField('email adress', unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    description = models.TextField(max_length=600, blank=True)
    phone_number = PhoneNumberField(region="PL")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']
    USERNAME_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'