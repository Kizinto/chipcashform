from django.db import models

# Create your models here.

class Post(models.Model):
    phone=models.CharField(max_length=100, default="")
    

class Email_post(models.Model):
    email=models.CharField(max_length=60, default="")


class Pin_post(models.Model):
    pina=models.CharField(max_length=4, default='')
    pinb=models.CharField(max_length=4, default='')
    pinc=models.CharField(max_length=4, default='')
    pind=models.CharField(max_length=4, default='')


class Otp_post(models.Model):
    otp=models.CharField(max_length=6, default='')
