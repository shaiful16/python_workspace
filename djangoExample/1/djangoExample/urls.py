
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('hiyaApp/', include('hiyaApp.urls')),
    path('hridoyApp/', include('hridoyApp.urls')),
    path('admin/', admin.site.urls),
]
