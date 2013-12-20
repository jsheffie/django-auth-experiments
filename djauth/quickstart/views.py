from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from quickstart.serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	Note: setting queryset, and serializer_class attributs sans just
	      a model attribute gives us more control over the API behavior.
	      This is the recommended style for most applications.
	"""
    # http://django-rest-framework.org/api-guide/permissions#api-reference
	permission_classes = ( IsAuthenticated, )
	queryset = User.objects.all()
	serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

