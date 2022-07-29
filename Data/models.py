from datetime import datetime
from django.db import models
from django.utils import timezone
from django.db.models.fields import IntegerField


class Mesa1(models.Model):

  fecha = models.DateField(default=timezone.now)
  garzon = models.CharField(max_length=20)
  subtotal = models.IntegerField()
  propina = models.IntegerField(null=True)
  total = models.IntegerField(null=True)
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

