from django.db import models
class Post(models.Model):
    name = models.CharField(max_length=100)
    idx = models.CharField(max_length=1000)
#Hej ovde ima nesto novo