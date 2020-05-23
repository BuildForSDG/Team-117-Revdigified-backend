from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import RDUser
from .serializers import RDUserSerializer

# Create your views here.
class Userlist(APIView):
    """
    list all users
    """
    def get(self, request, format=None):
        users = RDUser.objects.all()
        serializer = RDUserSerializer(users,many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = RDUserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


#class UserDetail(APIView):

