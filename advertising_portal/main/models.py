from django.db import models

# Create your models here.
class Offer(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    title = models.CharField(max_length=150)
    content = models.TextField(max_length = 10000)