from .serializers import NutritionCommoditySerializer, ScanningImageSerializer
from .models import NutritionCommodity, ScanningImage

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
import easyocr


class NutritionCommodityView(viewsets.ModelViewSet):
	queryset = NutritionCommodity.objects.all()
	serializer_class = NutritionCommoditySerializer


@api_view(['POST',])
def image_upload_and_scan(request):
    return Response({'method': 'POST', 'data': request.data})

# http://localhost:8000/media/scan_pics/2022-08-12%2003%3A13%3A04.520690%2B00%3A00/mallasahajraj%40gmail.com/Screen_Shot_2022-07-1_IvCuiwC.png

class ScanningImageView(viewsets.ModelViewSet):
	queryset = ScanningImage.objects.all()
	serializer_class = ScanningImageSerializer

	# authentication_classes = (TokenAuthentication,)
	# permission_classes = (IsAuthenticated,)


	def post(self, request, *args, **kwargs):
		user_id = request.data['user_id']
		image_to_scan = request.data['image_to_scan']
		ScanningImage.objects.create(user_id=user_id, image_to_scan=image_to_scan)

		ScanningImage.objects.all().order_by('-id')[0].image_to_scan.url
		reader = easyocr.Reader(["en"])

		results = reader.readtext(ScanningImage)


		return HttpResponse({'message': results}, status=200)