from .models import Duck
from rest_framework import serializers

class Duck_Serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Duck
		fields = ('id', 'duckname', 'ducklastname','duckmail', 'duckage')