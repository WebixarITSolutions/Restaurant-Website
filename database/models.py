from django.db import models

class Contactd(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    data=models.TextField(max_length=150)

class Feedbackd(models.Model):
    name1=models.CharField(max_length=20)
    email1=models.EmailField()
    num=models.IntegerField()
    feed=models.TextField()

class Reserved(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    uname1=models.TextField()
    email2=models.EmailField()
    num1=models.IntegerField()
    Time=models.CharField(max_length=20)
