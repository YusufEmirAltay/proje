from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<tur_adi>', views.details),
    path('kategori/<int:category_id>', views.getTurlarByCategoryId),
    path('kategori/<str:category_name>', views.getTurlarByCategory, name='turlar_by_category'),
    
    
]
