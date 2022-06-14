from django.urls import path,include
from . import views
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('about_company/', views.about_company, name='about_company'),
    path('business/', views.about_business, name='about_business'),
    path('social_media/', views.socialMedia, name='socialMedia'),
    path('new/<int:pk>/', views.new_detail, name='new_detail'),
    path('new/create/', views.news_create, name='news_create'),
    path('new/<int:pk>/edit/', views.news_edit, name='news_edit'),
    path('new/<pk>/remove/', views.news_remove, name='news_remove'),
    # path('scookie',views.setcookie, name='setcookie'),  
    # path('gcookie',views.getcookie, name='getcookie'),
    path('i18n/', include('django.conf.urls.i18n')),
]

