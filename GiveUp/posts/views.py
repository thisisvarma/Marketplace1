from django.shortcuts import render, get_object_or_404
from .models import Goods
from django.contrib.auth.decorators import login_required


# Create your views here.
def default_home(request):

    goods = Goods.objects.all()
    return render(request, template_name='goods/index.html', context={'goods': goods})


@login_required
def item_details(request, id):

    item_details = get_object_or_404(Goods, id=id)
    return render(request=request, template_name='goods/item_details.html', context={
        'item_details': item_details,
    })