# Generated by Django 3.1.5 on 2021-02-26 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShoppingApp', '0002_auto_20210226_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(choices=[('None', 'N/A'), ('red', 'Red'), ('black', 'Black'), ('white', 'White'), ('blue', 'Blue')], default='None', max_length=5),
        ),
        migrations.AlterField(
            model_name='product',
            name='ram',
            field=models.CharField(choices=[('None', 'N/A'), ('2', '2GB'), ('3', '3GB'), ('4', '4GB'), ('6', '6GB'), ('8', '8GB'), ('16', '16GB'), ('32', '32GB')], default='None', max_length=5),
        ),
        migrations.AlterField(
            model_name='product',
            name='storage',
            field=models.CharField(choices=[('None', 'N/A'), ('16', '16GB'), ('32', '32GB'), ('64', '64GB'), ('128', '128GB'), ('256', '256GB'), ('512', '512GB'), ('1024', '1TB')], default='None', max_length=5),
        ),
    ]
