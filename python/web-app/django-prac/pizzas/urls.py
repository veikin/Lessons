from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('store/', views.store, name='store'),
        path('toppings/<int:store_id>/', views.store, name='store'),
]
