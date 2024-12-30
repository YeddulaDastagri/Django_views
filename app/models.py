from django.db import models

# Create your models here. 
class Topic(models.Model):
    topicname=models.CharField(max_length=100,primary_key=True)

class WebPages(models.Model):
    topicname=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    urls=models.URLField() 
    email=models.EmailField() 
    

class AccessRecords(models.Model):
    name=models.ForeignKey(WebPages,on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    date=models.DateField()


