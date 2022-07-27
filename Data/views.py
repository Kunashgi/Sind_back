from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Data.models import Mesa1, Mesa2
from Data.serializers import Mesa1Serializer, Mesa2Serializer

@csrf_exempt
def mesa1Api(request, id=0):
  if request.method == 'GET':
    mesa1 = Mesa1.objects.all()
    mesa1_serializer = Mesa1Serializer(mesa1, many=True)
    return JsonResponse(mesa1_serializer.data, safe=False)

  elif request.method=='POST':
    mesa1_data=JSONParser().parse(request)
    mesa1_serializer = Mesa1Serializer(data=mesa1_data)
    if mesa1_serializer.is_valid():
      mesa1_serializer.save()
      return JsonResponse("agregado con exito,", safe=False)
    return JsonResponse("failed to Add",safe=False)

  elif request.method=='PUT':
    mesa1_data = JSONParser().parse(request)
    mesa1 = Mesa1.objects.get(ID=mesa1_data['ID'])
    mesa1_serializer = Mesa1Serializer(mesa1,data=mesa1_data)
    if mesa1_serializer.is_valid():
      mesa1_serializer.save()
      return JsonResponse("Update succesfull", safe=False)
    return JsonResponse ("failed update," ,safe=False)

  elif request.method=='DELETE':
    mesa1=Mesa1.objects.get(ID=id)
    mesa1.delete()
    return JsonResponse("delete sucessfull", safe=False)
