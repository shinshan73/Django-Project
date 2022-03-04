from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products', views.products, name='products'),

    path('create_product/', views.createProduct, name='create_product'),
    path('info_product/', views.infoProduct, name='info_product'),
        path('delete_product/<str:pk>', views.deleteProduct, name='delete_product')

    
]
