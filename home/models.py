from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class userdata(models.Model):
    lastName = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    formEmail = models.CharField(max_length=100)
    passportNumber = models.CharField(max_length=100)
    citizenship = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    visaCategory = models.CharField(max_length=100)
    def getEmail(self):
        return self.user.email
class availability(models.Model):
    url = models.CharField(max_length=100)
    def __str__(self):
        return self.url