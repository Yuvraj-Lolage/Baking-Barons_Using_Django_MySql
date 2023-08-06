# Generated by Django 4.0.6 on 2023-04-28 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BakersApp', '0004_anniversarycakes_cake_flavour_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
                ('Cake_Name', models.CharField(max_length=100)),
                ('Cake_Quantity', models.IntegerField()),
                ('CakePrice', models.IntegerField()),
                ('Cake_Size', models.CharField(max_length=500)),
                ('TotalPrice', models.IntegerField()),
            ],
        ),
    ]
