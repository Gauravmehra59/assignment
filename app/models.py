from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.
class contact(models.Model):
    Name1 =models.CharField(max_length=50, default='not available')
    Emaill=models.EmailField(max_length=50,default='not available')
    Phone_no =models.BigIntegerField(default='not available')
    Msg =models.CharField(max_length=100,default='not available')

class register(models.Model):
    reg_name = models.CharField(max_length=50)
    reg_email = models.EmailField(max_length=50)
    reg_phone = models.BigIntegerField()
    reg_address = models.CharField(max_length=50)
    reg_password = models.CharField(max_length=50)

class Imgsdata(models.Model):
    Imagename = models.CharField(max_length=50)
    Image = models.ImageField(upload_to="app/img/")