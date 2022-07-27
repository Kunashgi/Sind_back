from django.db import models
from django.db.models.fields import IntegerField

class Mesa1(models.Model):
  fecha = models.DateField()
  garzon = models.CharField(max_length=20)
  subtotal = models.IntegerField()
  propina = models.IntegerField()
  total = models.IntegerField()
  pago = models.CharField(max_length=20)
  ID = models.AutoField(primary_key=True)

class Mesa2(models.Model):
  fecha = models.DateField()
  garzon = models.CharField(max_length=20)
  subtotal = models.IntegerField()
  propina = models.IntegerField()
  total = models.IntegerField()
  pago = models.CharField(max_length=20)
  ID = models.AutoField(primary_key=True)

