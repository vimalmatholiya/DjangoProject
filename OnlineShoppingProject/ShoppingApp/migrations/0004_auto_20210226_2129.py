# Generated by Django 3.1.5 on 2021-02-26 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShoppingApp', '0003_auto_20210226_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(choices=[('red', 'Red'), ('black', 'Black'), ('white', 'White'), ('blue', 'Blue')], default='black', max_length=5),
        ),
    ]
