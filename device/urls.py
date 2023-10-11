from django.urls import path
from device import views

urlpatterns = [
    path('', views.device_add, name='device_add'),
    path('<str:deviceId>/', views.device_get, name='device_get'),
]