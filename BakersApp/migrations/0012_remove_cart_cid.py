# Generated by Django 4.0.6 on 2023-04-30 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BakersApp', '0011_rename_cake_id_cart_cid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='Cid',
        ),
    ]
