# Generated by Django 4.0.6 on 2023-05-05 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BakersApp', '0016_alter_tutorialvideo_video_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Feedback_Email', models.CharField(max_length=1000)),
                ('Feedback_Quality', models.CharField(max_length=50)),
                ('Feedback_Description', models.TextField(max_length=1000)),
                ('Feedback_StarRating', models.CharField(max_length=1000)),
            ],
        ),
    ]