from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from address.models import AddressField


class GoodsUsageLevel(models.Model):

    usage_level = models.CharField(max_length=25, null=False)

    def __str__(self):
        return self.usage_level


class GoodsCategory(models.Model):

    category = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.category


class GoodsStatus(models.Model):

    goods_status = models.CharField(max_length=25)

    def __str__(self):
        return self.goods_status


class GoodsManufacturer(models.Model):

    manufacturer_name = models.CharField(max_length=25)
    manufacturer_description = models.TextField()
    manufacturer_phonenumber = models.CharField(max_length=11, null=True, blank=True)
    manufacturer_location = AddressField()
    manufacturer_website = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return self.manufacturer_name


# Create your models here.
class Goods(models.Model):

    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False)
    posted_date = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=125)
    location = models.CharField(max_length=25, blank=False, null=False)
    goods_image = models.ImageField(upload_to="images/", default="img.png")
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    usage_level = models.ForeignKey(GoodsUsageLevel, on_delete=models.CASCADE, null=True, default='NotGiven')
    goods_category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, null=True)
    goods_status = models.ForeignKey(GoodsStatus, on_delete=models.CASCADE, null=True)
    manufacturer_name = models.ForeignKey(GoodsManufacturer, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = "goods"

    def __str__(self):
        return self.title


