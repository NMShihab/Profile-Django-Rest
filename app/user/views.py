from django.http import request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers


class DummyApiView(APIView):
    """Test API"""

    serializer_class = serializers.DummySerializer

    def get(self, request,format=None):
        """Return's list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'This is a Dummy api',
        ]

        return Response({"message":"Hello","an_apiview":an_apiview})

    def post(self,request):
        """Create a hello message with input name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f'Hello {name}!'
            return Response({'message':message})

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})
