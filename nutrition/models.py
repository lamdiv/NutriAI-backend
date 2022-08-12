from django.db import models
from home.models import User


class NutritionCommodity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nutrition_id = models.AutoField(primary_key=True)
    food_commodity = models.CharField(max_length=255)
    edible_portion = models.IntegerField(blank=True, null=True)
    moisture_g = models.IntegerField(blank=True, null=True)
    protein_g = models.IntegerField(blank=True, null=True)
    fat_g = models.IntegerField(blank=True, null=True)
    carbohydrate_h = models.IntegerField(blank=True, null=True)
    mineral_g = models.IntegerField(blank=True, null=True)
    fiber_g = models.IntegerField(blank=True, null=True)
    energy_k_cal = models.IntegerField(blank=True, null=True)
    calcium_mg = models.IntegerField(blank=True, null=True)
    phosphorous_mg = models.IntegerField(blank=True, null=True)
    iron_mg = models.IntegerField(blank=True, null=True)
    carotene_miu_g = models.IntegerField(blank=True, null=True)
    vitamin_c_mg = models.IntegerField(blank=True, null=True)
    thiamine_mg = models.IntegerField(blank=True, null=True)
    riboflavin_mg = models.IntegerField(blank=True, null=True)
    niacin_mg = models.IntegerField(blank=True, null=True)


    created_date =   models.DateTimeField(verbose_name="commodity_created", auto_now_add=True)
    updated_date =    models.DateTimeField(verbose_name="commodity_updated", auto_now=True)
    
    def __str__(self):
        return self.food_commodity