# Generated by Django 3.1.5 on 2021-03-04 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShoppingApp', '0012_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='deliveryDays',
            field=models.IntegerField(default=4),
        ),
    ]
