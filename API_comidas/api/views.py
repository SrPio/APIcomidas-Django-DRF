from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Plato, Alimento
from .serlializers import PlatoSerializer, AlimentoSerializer
from rest_framework import serializers
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


# Create your views here.
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_platos': 'all/',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/plato/pk/delete'
    }
    
    return Response(api_urls)


class PlatosViewSet(viewsets.ModelViewSet):
   queryset = Plato.objects.all()
   serializer_class = PlatoSerializer
   

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