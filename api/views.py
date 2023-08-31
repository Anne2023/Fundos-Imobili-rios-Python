from django.shortcuts import render
from rest_framework import viewsets,permissions
from api.models import FundoImobiliario
from api.serializers import FundoIobiliarioSerializers

# Create your views here.
class FundoImobiliarioViewsSet(viewsets.ModelViewSet):
    queryset = FundoImobiliario.objects.all() #configura  base para ser utilizado pela API, ele é utilizado na ação de listar, por exemplo
    serializer_class = FundoIobiliarioSerializers #configura qual serializer deverpa ser usado para conruir dado que cheam á API e produzir dados que seram enviados como resposta
    permission_classes = [permissions.IsAuthenticated] #lista contendo permissõe necessárias para acessar o endpoint exposto por essas viewSet. nsse cado irá permitir apenas o acesso a usuarios autenticados
