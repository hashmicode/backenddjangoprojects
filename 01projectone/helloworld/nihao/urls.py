from django.urls import path

from . import views

urlpatterns = [
    path('nihao/', views.nihaoPageView, name='nihaoPageView'),
]
