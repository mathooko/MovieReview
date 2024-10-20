from django.shortcuts import render
from .models import Users
from rest_framework import viewsets
from .serializers import UserSerializers
from rest_framework.response import Response

class CohortViewSet(viewsets.Viewset):
    """
    Viewset-> class based view that does not provide any method handlers for your requests
    View-> Python function or class that accepts HTTP requests and returns response
    """
# Create your views here.
    
    def list(self, request):
        queryset=Users.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset= Users.objects.all()
        serializer= UsersSerializer(queryset)
        return Response(serializer.data)
    
    def create(self, request):
        queryset = Users.objects.create(**request.data)
        serializer= UsersSerializer(queryset)
    def update(self, request, pk =None):
        pass
    def partial_update(self, request, pk):
        pass