from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import default_home, item_details

urlpatterns = [
    path('', default_home, name='home'),
    path('itemdetails/<int:id>/', item_details, name='itemdetails'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
