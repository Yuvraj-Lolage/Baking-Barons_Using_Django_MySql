# Generated by Django 4.0.6 on 2023-04-28 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BakersApp', '0007_cakes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cakes',
            name='category',
            field=models.IntegerField(),
        ),
    ]
