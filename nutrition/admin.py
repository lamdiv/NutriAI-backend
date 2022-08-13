from django.contrib import admin
from .models import NutritionCommodity, ScanningImage


class NutritionCommodityAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating','disease_varience')
    fields = [
        'name',
        'thumbnail',
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
        'rating',
        'disease_varience'
            ]
    

    class Meta:
        model = NutritionCommodity


admin.site.register(NutritionCommodity, NutritionCommodityAdmin)
admin.site.register(ScanningImage)
