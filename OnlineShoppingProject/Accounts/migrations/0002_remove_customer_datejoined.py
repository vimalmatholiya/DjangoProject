# Generated by Django 3.1.5 on 2021-02-17 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='dateJoined',
        ),
    ]
