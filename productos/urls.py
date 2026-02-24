from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.producto_list),
    path('productos/<int:pk>/', views.producto_detail),
]