from .models import Goods
from django import forms


class ListGoodsForSaleForm(forms.ModelForm):

    class Meta:
        model = Goods
        fields = ('title', 'description', 'goods_image', 'usage_level', 'goods_category', 'price', 'location')
