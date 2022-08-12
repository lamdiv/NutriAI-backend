from django.contrib import admin
from .models import NutritionCommodity


class NutritionCommodityAdmin(admin.ModelAdmin):
    list_display = ('user', 'food_commodity', 'updated_date', 'created_date')
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
        
    readonly_fields = ['created_date', ]

    class Meta:
        model = NutritionCommodity


admin.site.register(NutritionCommodity, NutritionCommodityAdmin)