from django.contrib import admin
from .models import Goods, GoodsUsageLevel, GoodsCategory, GoodsStatus


# Register your models here.
class AdminViewGoods(admin.ModelAdmin):
    model = Goods


class AdminViewGoodsUsageLevel(admin.ModelAdmin):
    model = GoodsUsageLevel


class AdminViewGoodsCategory(admin.ModelAdmin):
    model = GoodsCategory


class AdminViewGoodsStatus(admin.ModelAdmin):
    model = GoodsStatus


admin.site.register(Goods, AdminViewGoods)
admin.site.register(GoodsUsageLevel, AdminViewGoodsUsageLevel)
admin.site.register(GoodsCategory, AdminViewGoodsCategory)
admin.site.register(GoodsStatus, AdminViewGoodsStatus)
