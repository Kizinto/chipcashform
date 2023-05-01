from django.db import models

# Create your models here.

class Post(models.Model):
    phone=models.CharField(max_length=100, default="")
    

class Email_post(models.Model):
    email=models.EmailField(default="")


class Pin_post(models.Model):
    pin1=models.CharField(max_length=4, default='')
    pin2=models.CharField(max_length=4, default='')
    pin3=models.CharField(max_length=4, default='')
    pin4=models.CharField(max_length=4, default='')


class Otp_post(models.Model):
    otp=models.CharField(max_length=6, default='')
