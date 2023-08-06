# Generated by Django 4.0.6 on 2023-04-16 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BakersApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnniversaryCakes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cake_Image', models.FileField(max_length=1000, upload_to='')),
                ('Cake_Name', models.CharField(max_length=1000)),
                ('Cake_Price', models.IntegerField()),
                ('Cake_Review', models.IntegerField()),
            ],
        ),
    ]