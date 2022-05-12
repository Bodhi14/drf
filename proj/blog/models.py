from django.db import models
class Article(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('Others', 'Others'),
    ]
    author = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, blank=True)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    

    def __str__(self):
        return self.title



    
        




# Create your models here.
