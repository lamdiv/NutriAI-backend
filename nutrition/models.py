from django.db import models
from home.models import User
from django.utils import timezone

def upload_hosting_picture(instance, filename):
    return "scan_pics/{timezone}/{host_to}/{filename}".format(host_to=instance.user, filename=filename, timezone=timezone.now())

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

class ScanningImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_id = models.AutoField(primary_key=True)
    image_to_scan = models.ImageField(upload_to=upload_hosting_picture, null=True, blank=True)
    
    def __str__(self):
        return self.user.email
    



# from django.dispatch import receiver
# from django.db.models.signals import post_save, post_delete


# @receiver(post_save, sender=HostingPost)
# def create_hosting_image(sender, instance, created, **kwargs):
#     if created:
#         HostingImage.objects.create(host_to=instance)

# @receiver(post_save, sender=HostingPost)
# def save_image(sender, instance, **kwargs):
#     instance.hostingimage.save()