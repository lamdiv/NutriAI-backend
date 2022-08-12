from django.urls import path, include
from rest_framework import routers
from .views import (
                     NutritionCommodityView,
                     ScanningImageView,
                     image_upload_and_scan
                     )

route = routers.DefaultRouter()
route.register('nutrition', NutritionCommodityView)
route.register('image', ScanningImageView)


urlpatterns = [
    path('', include(route.urls)),
    path('image_upload_and_scan/', image_upload_and_scan),

]