from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('/first', views.first, name="first"),
    path('/second', views.second, name="second"),
    path('/third', views.third, name="third")
]