from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models  import DataReact
from .serializers import DataSerializers


class ListData(ListAPIView):
    queryset = DataReact.objects.all()
    serializer_class = DataSerializers
    

# Create your views here.


