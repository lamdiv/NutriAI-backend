from unittest import result
from rest_framework import serializers
from .models import NutritionCommodity, ScanningImage


class NutritionCommoditySerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionCommodity
        fields = [
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
                'thumbnail',
                'riboflavin_mg',
                'thumbnail',
                'rating',
                'disease_varience'
            ]


class ScanningImageSerializer(serializers.ModelSerializer):
    image_to_scan=serializers.ImageField()
    class Meta:
        model = ScanningImage
        fields = [ 
                    'image_id',
                    'image_to_scan',
                ]
