from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Plato, Alimento
from .serlializers import PlatoSerializer
from rest_framework import serializers
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


# Create your views here.
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_platos': '/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/plato/pk/delete'
    }
    
    return Response(api_urls)

def create(self, validated_data):
        alimentos = validated_data.pop("alimentos_ids", None)
        validated_data["nombre"] = self.context["request"].user
        plato = Plato.objects.create(**validated_data)
        if alimentos:
            plato.alimentos.set(alimentos)

        return plato 

@api_view(['POST'])
def add_plato(request):
    item = PlatoSerializer(data=request.data)
  
    # validating for already existing data
    if Plato.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
  
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_platos(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        items = Plato.objects.filter(**request.query_param.dict())
    else:
        items = Plato.objects.all()
        serializer = PlatoSerializer(items, many=True)
  
    # if there is something in items else raise error
    if items:
        data = PlatoSerializer(items)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_platos(request, pk):
    item = Plato.objects.get(pk=pk)
    data = PlatoSerializer(instance=item, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_platos(request, pk):
    item = get_object_or_404(Plato, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)