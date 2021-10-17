from django.contrib import admin
from .models import Goods


# Register your models here.
class AdminViewGoods(admin.ModelAdmin):
    model = Goods


admin.site.register(Goods, AdminViewGoods)
