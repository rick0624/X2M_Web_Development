from django.urls import path,include
from . import views
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('company/', views.about_company, name='about_company'),
    path('business/', views.about_business, name='about_business'),
    path('product/', views.about_product, name='about_product'),
    path('social_media/', views.socialMedia, name='socialMedia'),
    path('new/<int:pk>/', views.new_detail, name='new_detail'),
    path('new/create/', views.news_create, name='news_create'),
    path('new/<int:pk>/edit/', views.news_edit, name='news_edit'),
    path('new/<pk>/remove/', views.news_remove, name='news_remove'),
    path('contact/', views.contact_view, name='contact'),
    # path('scookie',views.setcookie, name='setcookie'),  
    # path('gcookie',views.getcookie, name='getcookie'),
    path('i18n/', include('django.conf.urls.i18n')),
    # path('test/<int:pk>/', views.test, name='test'),
]

