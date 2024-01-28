# Generated by Django 4.2.7 on 2024-01-27 16:48

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_type', models.CharField(choices=[('1', 'Room'), ('2', 'Local')], default='Room', max_length=15)),
                ('price', models.IntegerField(default=None)),
                ('size', models.FloatField(default=None)),
                ('capacity', models.IntegerField(default=None)),
                ('number_of_rooms', models.IntegerField(default=None)),
                ('img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('description', models.TextField(blank=True, max_length=10000)),
                ('address1', models.CharField(max_length=1024, verbose_name='Address line 1')),
                ('address2', models.CharField(max_length=1024, verbose_name='Address line 2')),
                ('zip_code', models.CharField(max_length=12, verbose_name='ZIP / Postal code')),
                ('city', models.CharField(max_length=1024, verbose_name='City')),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
        ),
    ]
