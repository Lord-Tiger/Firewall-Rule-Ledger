from django.shortcuts import render
from rest_framework import viewsets
from .models import FirewallRequest
from .serializers import FirewallRequestSerializer

# Create your views here.
class FirewallRequestViewSet(viewsets.ModelViewSet):
    queryset = FirewallRequest.objects.all()
    serializer_class = FirewallRequestSerializer
