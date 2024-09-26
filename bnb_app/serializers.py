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
	guest = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
	listing = serializers.PrimaryKeyRelatedField(queryset=Listing.objects.all())
	rating = serializers.PrimaryKeyRelatedField(queryset=Review.objects.all())

	def to_representation(self, instance):
		representation = super().to_representation(instance)
		representation['guest'] = instance.guest.username  # Access the name attribute
		representation['listing'] = instance.listing.title
		representation['rating'] = f"{instance.rating}"
		return representation

	class Meta:
		model = Review
		fields = ('id', 'guest', 'listing', 'rating', 'comment',)

