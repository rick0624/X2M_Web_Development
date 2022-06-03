from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('social_media/', views.socialMedia, name='socialMedia'),
    path('new/<int:pk>/', views.new_detail, name='new_detail'),
]