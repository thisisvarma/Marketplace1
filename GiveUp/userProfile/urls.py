from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import new_user_registration, login_request, logout_request, profile, profile_view


urlpatterns = [
    path('register', new_user_registration, name='register'),
    path('login', login_request, name='login'),
    path('logout', logout_request, name='logout'),
    path('profile', profile, name='profile'),
    url(r'^profile=(?P<username>\w+)/$', profile_view, name='profile_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
