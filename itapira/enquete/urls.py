from django.contrib import admin
from django.urls import path, include

from.import views

urlpatterns = [
    path('enquete/', include('enquete.urls')),
    path('', views.index, name='index'),
]