from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from address.models import AddressField

sex_choices = [
    ('male', 'male'),
    ('female', 'female'),
    ('other', 'other'),
    ('NA', 'NA'),
]


# Create your models here.
class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='userProfilePics/', default='avatar.png')
    sex = models.CharField(max_length=20, choices=sex_choices, default='NA')
    Bio = models.TextField(blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    facebook_id = models.CharField(max_length=25, blank=True, null=True)
    instagram_id = models.CharField(max_length=25, blank=True, null=True)
    twitter_id = models.CharField(max_length=25, null=True, blank=True)
    geo_location = models.CharField(max_length=55, null=True, blank=True)
    address = AddressField(on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.user} profile'

    # def save(self):
    #     super().save()
    #     img = Image.open(self.profile_pic.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.profile_pic.path)


@receiver(post_save, sender=User)
def create_userProfile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_UserProfile(sender, instance, **kwargs):
    instance.userprofile.save()