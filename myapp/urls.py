from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('link-clicked/<path:link_url>/', views.link_clicked, name='link_clicked'),
]
