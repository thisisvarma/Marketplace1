from django.shortcuts import render, get_object_or_404, redirect
from .models import Goods
from django.contrib.auth.decorators import login_required
from .forms import ListGoodsForSaleForm
from django.contrib import messages


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

@login_required
# @transaction.atomic
def list_goods_for_sale(request):
    
    if request.method == 'POST':
        itemforsale_form = ListGoodsForSaleForm(request.POST, request.FILES)

        if itemforsale_form.is_valid():
            post = itemforsale_form.save(commit=False)
            post.posted_by = request.user
            itemforsale_form.save()
            messages.success(request, message=f'You have posted items successfully \n {itemforsale_form.errors}')
            return redirect('home')
        else:
            messages.error(request, f'Please correct the error below. \n {itemforsale_form.errors}')
    else:
        itemforsale_form = ListGoodsForSaleForm()
    return render(request, template_name='goods/itemforsale.html', context={'itemforsale_form': itemforsale_form})