from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('age', views.getAge),
    path('getheight', views.getheight, name='getheight'),
]