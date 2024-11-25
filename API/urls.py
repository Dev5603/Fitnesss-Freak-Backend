from django.urls import path
from . import views

urlpatterns = [
    path('news', views.news),
    path('contact', views.contact),
    path('plans', views.plans)
]
