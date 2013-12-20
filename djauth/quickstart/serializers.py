from django.contrib.auth.models import User, Group
from rest_framework import serializers

# hyperlinking is good restful design.
class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		# note: that the django model for user has no 'url' or 'groups' fields
		#       which HyperlinkedModelSerializer is piggybacking on.
		fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		# note: group has no 'url' field... HyperlinkedModelSerializer is piggybacking on this
		fields = ('url', 'name')
