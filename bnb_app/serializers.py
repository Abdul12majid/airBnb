from rest_framework import serializers
from .models import Listing, Review
from django.contrib.auth.models import User

class PropSerializer(serializers.ModelSerializer):
	host = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

	def to_representation(self, instance):
		representation = super().to_representation(instance)
		representation['host'] = instance.host.username  # Access the name attribute
		return representation

	class Meta:
		model = Listing
		fields = ('id', 'title', 'description', 'location', 'is_available', 'amenities', 'host', )


class UrlSerializer(serializers.Serializer):
    endpoints=serializers.CharField(max_length=500)


class RevSerializer(serializers.ModelSerializer):
	class Meta:
		model = Review
		fields = ('id', 'guest', 'Listing', 'rating', 'comment',)