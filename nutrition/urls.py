from django.urls import path, include
from rest_framework import routers
from .views import (
                     NutritionCommodityView
                     )

route = routers.DefaultRouter()
route.register('nutrition', NutritionCommodityView)


urlpatterns = [
    path('', include(route.urls))
]