# Generated by Django 3.0.5 on 2020-07-11 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='mall',
        ),
        migrations.RemoveField(
            model_name='product',
            name='shipping_fee',
        ),
    ]
