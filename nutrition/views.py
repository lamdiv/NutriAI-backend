from .serializers import NutritionCommoditySerializer
from .models import NutritionCommodity
from rest_framework import viewsets



class NutritionCommodityView(viewsets.ModelViewSet):
	queryset = NutritionCommodity.objects.all()
	serializer_class = NutritionCommoditySerializer