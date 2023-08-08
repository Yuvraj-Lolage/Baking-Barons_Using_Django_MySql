from django.db import models

# Create your models here.
class BirthdayCakes(models.Model):
    Cake_Image = models.FileField(max_length=1000)
    Cake_Name = models.CharField(max_length=1000)
    Cake_Price = models.IntegerField()
    Cake_Review = models.IntegerField()
    Cake_Flavour = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.Cake_Name
    

class AnniversaryCakes(models.Model):
    Cake_Image = models.FileField(max_length=1000)
    Cake_Name = models.CharField(max_length=1000)
    Cake_Price = models.IntegerField()
    Cake_Review = models.IntegerField()
    Cake_Flavour = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.Cake_Name
    
  
class ThemeCakes(models.Model):
    Cake_Image = models.FileField(max_length=1000)
    Cake_Name = models.CharField(max_length=1000)
    Cake_Price = models.IntegerField()
    Cake_Review = models.IntegerField()
    Cake_Flavour = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.Cake_Name

class Cart(models.Model):
    userId = models.IntegerField()
    CakeId = models.IntegerField()
    username = models.CharField(max_length=100)
    Cake_Name = models.CharField(max_length=100)
    Cake_Image = models.FileField(max_length=1000)
    Cake_flavour = models.CharField(max_length=1000)
    Cake_Quantity = models.IntegerField()
    CakePrice = models.IntegerField()
    Cake_Size = models.CharField(max_length=500)
    TotalPrice = models.IntegerField()

    def __str__(self):
        return self.username
    

class Cakes(models.Model):
    Cake_Image = models.FileField()
    Cake_Name = models.CharField(max_length=1000)
    Cake_Price = models.IntegerField()
    Cake_Review = models.IntegerField()
    Cake_Flavour = models.CharField(max_length=1000)
    category = models.IntegerField() #1 = birthday   2= anniversary  3= themecake 4 = co0kie
    
    def __str__(self):
        return self.Cake_Name
    
class TutorialVideo(models.Model):
    Video_Title = models.CharField(max_length=1000)
    Video_File = models.FileField(max_length=100)
    Video_description = models.TextField(max_length=1000)
    Video_Thumbnail = models.FileField(max_length=500)
    
    def __str__(self):
        return self.Video_Title
    
class Feedback(models.Model):
    Feedback_Email = models.CharField(max_length=1000)
    Feedback_Quality = models.CharField(max_length=50)
    Feedback_Description = models.TextField(max_length=1000)
    Feedback_StarRating = models.CharField(max_length=1000)
    
    def __str__(self) -> str:
        return self.Feedback_Email