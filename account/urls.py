from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^api/token', obtain_jwt_token),
    url(r'^bucket/(?P<pk>\d+)', UserList.as_view()),
    url(r'^bucket/swap/(?P<pk>\d+)', UserList.as_view()),
    url(r'^(?P<pk>\d+)/', UserDetail.as_view()),
    url(r'^create/', UserCreate.as_view()),
]
