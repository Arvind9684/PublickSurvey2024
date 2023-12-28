from django.db import models

# Create your models here.
class contact_detail(models.Model):
    mobile=models.CharField(max_length=10,unique=True)
    country=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    date=models.CharField(max_length=15)
    time=models.CharField(max_length=10)
    def __str__(self):
        return self.mobile
class chat_detail(models.Model):
    mobile = models.ForeignKey(contact_detail, on_delete=models.CASCADE,null=False)
    country=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    Chat=models.CharField(max_length=500)
    Latitude=models.CharField(max_length=50)
    Longitude=models.CharField(max_length=50)
    date=models.CharField(max_length=15)
    time=models.CharField(max_length=10)
class public_votting(models.Model):
    mobile = models.ForeignKey(contact_detail, on_delete=models.CASCADE,null=False)
    country=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    party_name=models.CharField(max_length=50)
    Latitude=models.CharField(max_length=50)
    Longitude=models.CharField(max_length=50)
    date=models.CharField(max_length=15)
    time=models.CharField(max_length=10)
    result = models.IntegerField(default=1)

    

