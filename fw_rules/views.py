from django.shortcuts import render
from rest_framework import viewsets
from .models import FirewallRequest
from .serializers import FirewallRequestSerializer

# Create your views here.
class FirewallRequestViewSet(viewsets.ModelViewSet):    #This is referencing the object/class in the serializer file.
    queryset = FirewallRequest.objects.all()
    serializer_class = FirewallRequestSerializer
