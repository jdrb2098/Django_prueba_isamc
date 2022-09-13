from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from .serializers import *


@api_view(['GET'])
def getArticulos(request):
    query = request.query_params.get('keyword')
    if(query == None):
        query = ''
    articulos = Articulo.objects.filter(nombre__icontains = query).order_by("nombre")
    page = request.query_params.get("page")
    paginator = Paginator(articulos, 4)
    
    try:
        articulos = paginator.page(page)
    except PageNotAnInteger:
        articulos = paginator.page(1)
    except EmptyPage:
        articulos = paginator.page(paginator.num_pages)
    
    if page == None:
        page = 1

    page = int(page)
    serializer = ArticuloSerializer(articulos, many= True)
    return Response({'articulos': serializer.data, 'page': page, 'pages': paginator.num_pages}) 


# Create your views here.
