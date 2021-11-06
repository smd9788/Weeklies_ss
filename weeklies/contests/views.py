from django.http import HttpResponse

from .models import Contest, Security, SecurityPool
from .serializers import ContestSerializer, SecuritySerializer, SecurityPoolSerializer
from rest_framework import generics

class ContestListCreate(generics.ListCreateAPIView):
    queryset = Contest.objects.all()
    serializer_class = ContestSerializer

class SecurityListCreate(generics.ListCreateAPIView):
    queryset = Security.objects.all()
    serializer_class = SecuritySerializer

class SecurityPoolListCreate(generics.ListCreateAPIView):
    queryset = SecurityPool.objects.all()
    serializer_class = SecurityPoolSerializer