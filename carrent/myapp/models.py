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

class Rent(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    car=models.ForeignKey(Car,on_delete=models.CASCADE)
    start=models.DateTimeField()
    stop=models.DateTimeField()
    cost=models.DecimalField( max_digits=10, decimal_places=2)