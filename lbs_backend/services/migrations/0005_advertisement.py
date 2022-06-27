# Generated by Django 3.2.12 on 2022-06-08 06:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
        ('locations', '0001_initial'),
        ('services', '0004_auto_20220607_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ADText', models.TextField(blank=True, null=True)),
                ('Timestamp', models.DateTimeField(auto_now_add=True)),
                ('ExpiryDate', models.DateField(blank=True, null=True)),
                ('NoOfMessages', models.IntegerField(blank=True, null=True)),
                ('GenderID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='gender_advert', to='users.gender')),
                ('LocationID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='location_advert', to='locations.townsmodel')),
                ('ProductID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='product_advert', to='services.product')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_advert', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Advertisements',
                'verbose_name_plural': 'Advertisements',
            },
        ),
    ]