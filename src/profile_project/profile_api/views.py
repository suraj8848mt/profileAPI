from django.shortcuts import render

from rest_framework import viewsets

from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

from .serializer import HelloSerializer, UserProfileSerializer
from .permissions import UpdateOwnProfile

from .models import UserProfile
class HelloAPIView(APIView):
	''' Test Api View '''

	serializer_class = HelloSerializer

	def get(seld, request, format=None):

		an_apiview = [
		'uses Http method as function(GET, POST, PATCH, PUT, DELETE', 
		'It is similar to a traditional django view',
		'Gives The most control over your logic',
		'Is mapped manaully to URLs'
		]
		return Response({'message':'Hello', 'an_apiview':an_apiview})


	def post(self, request):
		''' Create a hlw message with our name '''

		serializer = HelloSerializer(data=request.data)

		if serializer.is_valid():
			name = serializer.data.get('name')
			message = 'Hello {0}'.format(name)
			return Response({'message':message})
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	def put(self, request, pk=None):
		''' Handles an updating objs '''
		return Response({'method': 'put'})

	def patch(self, request, pk=None):
		''' Handles an partial update '''
		return Response({'method':'patch'})

	def delete(self, request, pk=None):
		''' Delets ana objs '''
		return Response({"method":'delete'}) 

# List, Create, Retrieve, UPdate, Partial_Update
class HelloViewSet(viewsets.ViewSet):
	''' Test API VIEWSET '''

	serializer_class = HelloSerializer

	def list(self, request):
		''' Return a hello message '''
		a_viewset = [
		'uses actions (List, Create, Retrieve, UPdate, Partial_Update)',
		'Automatically maps to URLs using Routers',
		'Provides more functionally with less code'
		]
		return Response({'message':'Hello!', 'a_viewset':a_viewset})

	def create(self, request):
		''' Create a new hellow msg '''
		serializer = HelloSerializer(data= request.data)

		if serializer.is_valid():
			name = serializer.data.get('name')
			message = 'Hello {0}'.format(name)
			return Response({'message':message})
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def retrieve(self, request, pk=None):
		''' Handles getting an objs by an id '''
		return Response({'http_method': 'GET'})

	def update(self, request, pk=None):
		''' Handles updating an objs '''
		return Response({'http_method': 'PUT'})

	def partial_update(self, request, pk=None):
		''' Handles Updating part of an objs '''

		return Response({'http_method': 'PATCH'})

	def destroy(self, request, pk=None):
		''' Handles removing an objs. '''

		return Response({'http_method':'DELETE'})



class UserProfileViewSet(viewsets.ModelViewSet):
	''' Handels creating nad updatin profiles '''
	serializer_class = UserProfileSerializer

	queryset = UserProfile.objects.all()

	authentication_classes = (TokenAuthentication,)
	permission_classes = (UpdateOwnProfile,)



