from django.db import models

class webData(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phoneNo = models.CharField(max_length=10)
    email = models.EmailField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=100)

class UserInfo(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    house_no = models.CharField(max_length=100)
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Useridpas(models.Model):
    email = models.EmailField(max_length=300)
    password = models.CharField(max_length=100)

class feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=300)
    feedback = models.CharField(max_length=5000)
    
class message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=300)
    subject = models.CharField(max_length=1000)
    massege = models.CharField(max_length=5000)
    

    
    
