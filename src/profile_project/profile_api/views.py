from django.shortcuts import render
from rest_framework.views import  APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
	''' Test Api View '''
	def get(seld, request, format=None):

		an_apiview = [
		'uses Http method as function(GET, POST, PATCH, PUT, DELETE', 
		'It is similar to a traditional django view',
		'Gives The most control over your logic',
		'Is mapped manaully to URLs'
		]
		return Response({'message':'Hello', 'an_apiview':an_apiview})


