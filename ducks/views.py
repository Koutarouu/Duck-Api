from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Duck
from .serializers import Duck_Serializer

class DuckList(generics.ListCreateAPIView):
	queryset = Duck.objects.all()
	serializer_class = Duck_Serializer

	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(
			queryset,
			pk = self.kwargs['pk'],
		)
		return obj
