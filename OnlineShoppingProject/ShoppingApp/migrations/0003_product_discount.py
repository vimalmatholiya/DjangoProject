# Generated by Django 3.1.5 on 2021-02-20 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShoppingApp', '0002_auto_20210220_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=0),
        ),
    ]
