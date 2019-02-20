from django.db import models

class Customer(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    dob=models.DateField()
    tel=models.CharField(max_length=10)

class Car(models.Model):
    brand=models.CharField(max_length=10)
    price=models.DecimalField( max_digits=10, decimal_places=2)
    purchasing_date=models.DateField()