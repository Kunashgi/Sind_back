from rest_framework import serializers
from Data.models import Mesa1, Mesa2

class Mesa1Serializer(serializers.ModelSerializer):
  class Meta:
    model = Mesa1
    fields = ('fecha', 'garzon', 'subtotal', 'propina', 'total', 'pago', 'ID')

class Mesa2Serializer(serializers.ModelSerializer):
  class Meta:
    model = Mesa2
    fields = ('fecha', 'garzon', 'subtotal', 'propina', 'total', 'pago', 'ID')
