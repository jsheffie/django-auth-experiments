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
	ret_str = "Hello Authenticated user required. "
	ret_str += "<br>User: %s" % ( request.user.username )
	ret_str +="<br><a href='/logout/'>Logout</a>"
	return HttpResponse( ret_str );

def no_auth_view( request ):
	ret_str = "No Authenticated user required"
	ret_str += "<br>User: %s" % ( request.user.username )
	ret_str += "<br><a href='/auth/view/'>Auth Required</a>"
	ret_str += "<br><a href='/no/auth/view/'>No Auth Required</a>"
	ret_str +="<br><a href='/logout/'>Logout</a>"
	return HttpResponse( ret_str );

@login_required
def auth_view( request ):
	ret_str = "Authenticated user required"
	ret_str += "<br>User: %s" % ( request.user.username )
	ret_str += "<br><a href='/auth/view/'>Auth Required</a>"
	ret_str += "<br><a href='/no/auth/view/'>No Auth Required</a>"
	ret_str +="<br><a href='/logout/'>Logout</a>"
	return HttpResponse( ret_str );

def logout_view(request):
	logout( request )
	return HttpResponseRedirect(redirect_to="/no/auth/view/");


