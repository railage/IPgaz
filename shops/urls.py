from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('shop/<int:shop_id>/', views.shop_detail, name='shop_detail'),
    path('shop/<int:shop_id>/category/<int:category_id>/', views.category_detail, name='category_detail'),
]