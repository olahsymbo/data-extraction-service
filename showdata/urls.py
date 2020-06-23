from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from . import views

routers = routers.DefaultRouter()

urlpatterns = [
    url(r'retrieve/', views.showtask.as_view(), name=None),
    url('index.html/', views.showtask.index)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)