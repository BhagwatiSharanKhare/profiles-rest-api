from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets

class HelloApiView(APIView):
    """ Test API View """
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """ returns a list of APIView features"""
        an_apiview = [
        'Uses Http Method as function (get, post, patch, put, delete)',
        'Is similar to traditional Django View',
        'Gives you most control over application logic',
        'Is mapped manually to urls'
        ]
        return Response({
        'message':'hello',
        'an_apiview': an_apiview
        # need to return a list or dictionary the object is converted into json
        })

    def post(self, request, format=None):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({
            'message':message
            })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """ handle updating an object"""
        return Response({
        'method': 'Put'
        })

    def patch(self, request, pk=None):
        """ handle a partial update of an object"""
        return Response({
        'method': 'Patch'
        })

    def delete(self, request, pk=None):
        """ Delete an object"""
        return Response({
        'method': 'Delete'
        })


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ return a hello message"""
        a_viewset= [
         'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]
        return Response({
        'message':'hello',
        'a_viewset': a_viewset
        })


    def create(self, request):
        """create a new hello message"""

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({
            'message':message
            })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """ handle getting an object by it's id"""
        return Response({
        'http_method': 'GET'
        })

    def update(self, request, pk=None):
        """ handle updating an object"""
        return Response({
        'http_method': 'PUT'
        })

    def partial_update(self, request, pk=None):
        """ handle updating part of an object"""
        return Response({
        'http_method': 'PATCH'
        })

    def destroy(self, request, pk=None):
        """ handle removing an object"""
        return Response({
        'http_method': 'DELETE'
        })
