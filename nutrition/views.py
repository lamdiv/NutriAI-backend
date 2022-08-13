from typing import final
from .serializers import NutritionCommoditySerializer, ScanningImageSerializer
from .models import NutritionCommodity, ScanningImage
import os
from pathlib import Path
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
import easyocr
from rest_framework.filters import SearchFilter, OrderingFilter
import csv

BASE_DIR = Path(__file__).resolve().parent.parent
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

class NutritionCommodityView(viewsets.ModelViewSet):
	queryset = NutritionCommodity.objects.all()
	serializer_class = NutritionCommoditySerializer
	filter_backends = (SearchFilter, OrderingFilter)
	
	search_fields = (
					'name',
					'protein_g',
					'fat_g',
					'carbohydrate_h',
					'mineral_g',
					'fiber_g',
					'energy_k_cal',
					'calcium_mg',
					'phosphorous_mg',
					'iron_mg',
					'carotene_miu_g',
					'vitamin_c_mg',
					'thiamine_mg',
					'riboflavin_mg',
				
				)

	def list(self,request,*args,**kwargs):
		return super().list(request,*args,**kwargs)
		

@api_view(['POST',])
def image_upload_and_scan(request):
	image_to_scan_url = request.data["image_to_scan"]
	reader = easyocr.Reader(["en"])
	results = reader.readtext(image_to_scan_url)	
	return Response({'method': 'POST', 'image_to_scan_url': image_to_scan_url, "results": results})

# http://localhost:8000/media/scan_pics/2022-08-12%2003%3A13%3A04.520690%2B00%3A00/mallasahajraj%40gmail.com/Screen_Shot_2022-07-1_IvCuiwC.png

class ScanningImageView(viewsets.ModelViewSet):
	queryset = ScanningImage.objects.all()
	serializer_class = ScanningImageSerializer

	# authentication_classes = (TokenAuthentication,)
	# permission_classes = (IsAuthenticated,)


	def post(self, request, *args, **kwargs):
		image_to_scan = request.data['image_to_scan']
		new_image=ScanningImage.objects.create( image_to_scan=image_to_scan)
		reader = easyocr.Reader(["en"])
		image_url=str(BASE_DIR)+str(new_image.image_to_scan.url)
		results = reader.readtext(image_url)		
		return Response({'method': 'POST', 'image_to_scan_url': new_image.image_to_scan.url, "results": results})


		# image_path = ScanningImage.objects.all().order_by('-image_id')[0].image_to_scan.url
		# reader = easyocr.Reader(["en"])
		# print(image_path)
		# results = reader.readtext(image_path)	


		# return Response({"results": results})
