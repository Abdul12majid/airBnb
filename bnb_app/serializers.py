from rest_framework import serializers
from .models import Listing

class PropSerializer(serializers.ModelSerializer):
	class Meta:
		model = Listing
		fields = ('id', 'title', 'description', 'location', 'is_available', 'amenities', 'host', )