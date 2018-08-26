from account.models import User
from account.serializers import UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.decorators import api_view,permission_classes


@api_view(['POST'])
@permission_classes([AllowAny, ])
def authenticate_user(request):
	print("authenticating user")
	try:
		email = request.data['email']
		password = request.data['password']
		user = User.objects.get(email=email, password=password)
		if user:
			try:
				payload = jwt_payload_handler(user)
				token = jwt.encode(payload, settings.SECRET_KEY)
				user_details = {}
				user_details['name'] = "%s %s" % (
					user.first_name, user.last_name)
				user_details['token'] = token
				user_logged_in.send(sender=user.__class__,
									request=request, user=user)
				return Response(user_details, status=status.HTTP_200_OK)
 
			except Exception as e:
				raise e
		else:
			res = {
				'error': 'can not authenticate with the given credentials or the account has been deactivated'}
			return Response(res, status=status.HTTP_403_FORBIDDEN)
	except KeyError:
		res = {'error': 'please provide a email and a password'}
		return Response(res)


class UserList(APIView):
	permission_class = [IsAuthenticated]

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
	permission_class = [IsAuthenticated]

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
	permission_classes = [IsAuthenticated]
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
		



