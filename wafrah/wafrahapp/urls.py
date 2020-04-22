from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='index'),
    path('categories', views.categories, name='categories'),
    path('productView', views.productView, name='productView'),
]