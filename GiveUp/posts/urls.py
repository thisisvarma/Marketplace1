from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import default_home, item_details, list_goods_for_sale

urlpatterns = [
    path('', default_home, name='home'),
    path('itemdetails/<int:id>/', item_details, name='itemdetails'),
    path('listforsale', list_goods_for_sale, name='listforsale'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
