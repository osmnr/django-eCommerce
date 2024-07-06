from django.urls import path
from . import views

app_name = 'shop'


urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('shop/', views.shop, name = 'shop'),
    path('shopgrid/', views.shopgrid, name = 'shopgrid'),
    path('shopdetail/', views.shopdetail, name = 'shopdetail'),
]
