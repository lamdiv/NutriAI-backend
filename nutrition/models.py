from distutils.command.upload import upload
from django.db import models
from home.models import User
from django.utils import timezone

def upload_hosting_picture(instance, filename):
    return "scan_pics/{filename}".format(filename=filename)

class NutritionCommodity(models.Model):

    CHOICES = (
        ('Low','Low'),
        ('Neutral','Neutral'),
        ('High','High'),
    )

    name = models.CharField(max_length=255)
    protein_g = models.FloatField(blank=True, null=True)
    fat_g = models.FloatField(blank=True, null=True)
    carbohydrate_h = models.FloatField(blank=True, null=True)
    mineral_g = models.FloatField(blank=True, null=True)
    fiber_g = models.FloatField(blank=True, null=True)
    energy_k_cal = models.FloatField(blank=True, null=True)
    calcium_mg = models.FloatField(blank=True, null=True)
    phosphorous_mg = models.FloatField(blank=True, null=True)
    iron_mg = models.FloatField(blank=True, null=True)
    carotene_miu_g = models.FloatField(blank=True, null=True)
    vitamin_c_mg = models.FloatField(blank=True, null=True)
    thiamine_mg = models.FloatField(blank=True, null=True)
    riboflavin_mg = models.FloatField(blank=True, null=True)

    thumbnail = models.ImageField(upload_to='food', null=True)
    rating = models.PositiveIntegerField(default=1)
    disease_varience = models.CharField(max_length=20,choices=CHOICES, default='Neutral')
    
    def __str__(self):
        return self.name

class ScanningImage(models.Model):
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