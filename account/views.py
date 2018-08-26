from account.models import User
from account.serializers import UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.permissions import AllowAny,IsAuthenticated

class UserList(APIView):
	#permission_class = [AllowAny]

	def get(self, request, pk, format=None):
		users = User.objects.filter(bucket=pk)
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data,status=200)
	
	def put(self, request, pk, format=None):
		user = User.objects.get(pk=pk)
		serializer = UserSerializer(user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=200)
		return JsonResponse(serializer.errors, status=400)


class UserCreate(APIView):

	def post(self,request,format=None):
		serializer = UserSerializer(data=request.data)
		bucket = request.data['bucket']
		tenants = User.objects.filter(bucket=bucket)
		print(len(tenants))

		if len(tenants)==20:
			message = {'message':'Select another bucket'}
			return JsonResponse(message, status=400)

		if serializer.is_valid():
			serializer.validated_data
			serializer.save()
			return JsonResponse(serializer.data, status=201)

		return JsonResponse(serializer.errors,status=400)


class UserDetail(APIView):
	def get_user_object(self, pk):
		try:
			return User.objects.get(pk=pk)	
		except User.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		user = self.get_user_object(pk)
		serializer = UserSerializer(user)
		return JsonResponse(serializer.data, status=200)

	def put(self, request, pk, format=None):
		user = self.get_user_object(pk)
		serializer = UserSerializer(user, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=200)
		return JsonResponse(serializer.errors, status=400)

	def delete(self, request, pk, format=None):
		user = self.get_user_object(pk)
		user.delete()
		return JsonResponse(status=204)		
		



