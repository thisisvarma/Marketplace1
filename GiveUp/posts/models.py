from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Goods(models.Model):

    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False)
    posted_date = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=125)
    location = models.CharField(max_length=25, blank=False, null=False)
    goods_image = models.ImageField(upload_to="images/", default="img.png")
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "goods"

    def __str__(self):
        return self.title

