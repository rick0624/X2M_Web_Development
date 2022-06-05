from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('social_media/', views.socialMedia, name='socialMedia'),
    path('new/<int:pk>/', views.new_detail, name='new_detail'),
    path('new/create/', views.news_create, name='news_create'),
    path('new/<int:pk>/edit/', views.news_edit, name='news_edit'),
    path('new/<pk>/remove/', views.news_remove, name='news_remove'),
    # path('scookie',views.setcookie, name='setcookie'),  
    # path('gcookie',views.getcookie, name='getcookie'),
]