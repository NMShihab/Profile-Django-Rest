from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class DummyApiView(APIView):
    """Test API"""

    def get(self, request,format=None):
        """Return's list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'This is a Dummy api',
        ]

        return Response({"message":"Hello","an_apiview":an_apiview})





