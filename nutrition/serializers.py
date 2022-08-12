from rest_framework import serializers
from .models import NutritionCommodity, ScanningImage


class NutritionCommoditySerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionCommodity
        fields = [
                'user',
                'food_commodity',
                'edible_portion',
                'moisture_g',
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
                'niacin_mg',
            ]


class ScanningImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScanningImage
        fields = [ 
                    'user',
                    'image_id',
                    'image_to_scan'
                ]
