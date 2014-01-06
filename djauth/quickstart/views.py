from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required

from quickstart.serializers import UserSerializer, GroupSerializer

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout

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

@login_required
def testing_users( request ):
	return HttpResponse("Hello authenticated user %s <br><a href='/logout/'>Logout</a>" % ( request.user.username ));

def logout_view(request):
	logout( request )
	return HttpResponseRedirect(redirect_to="/testing_users/");


