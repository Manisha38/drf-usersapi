from rest_framework.views import APIView
from rest_framework.decorators import api_view,parser_classes
from rest_framework.response import Response
from django.core import serializers
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
import json
from .models import User
from .serializers import UserSerializer


@api_view(['GET'])
def list_all(request):
	users = User.objects.all()
	useremails = [user.id for user in users]
	return Response(useremails)


@api_view(['GET','PUT'])
def user_detail(request,user_id):
	if request.method=='GET':
		user = User.objects.get(id=user_id)
		serializer = UserSerializer(user) 
		return Response(serializer.data)
	if request.method=='PUT':	
		data = JSONParser().parse(request)
		user = User.objects.get(id=user_id)
		serializer = UserSerializer(user, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)
	if request.method=='DELETE':
		user = User.objects.get(id=user_id)
		user.delete()
		return Response(status=200)


@api_view(['POST'])
#@parser_classes({JSONParser,})
def creat_user(request):
	data = str(request.body,encoding='utf-8')
	print(data)
	jdata = json.loads(data)
	print("dkjsgdn")

	serializer = UserSerializer(data=jdata)
	if serializer.is_valid():
		serializer.save()
		serializer.validated_data
		return JsonResponse(serializer.data,status=201)
	else:
		print(serializer)
		return JsonResponse(serializer.errors, status=400)

