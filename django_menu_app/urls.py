"""
URL configuration for django_menu_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django_menu_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contacts/', views.contacts, name='contacts'),
    path('services/web-dev/', views.web_dev, name='web_dev'),
    path('services/mobile-apps/', views.mobile_apps, name='mobile_apps'),
    path('secondary/', views.secondary, name='secondary'),
    path('secondary/news/', views.news, name='news'),
    path('secondary/blog/', views.blog, name='blog'),
    path('secondary/portfolio/', views.portfolio, name='portfolio'),
    path('secondary/portfolio/web-projects/', views.web_projects, name='web_projects'),
    path('secondary/portfolio/mobile-apps/', views.mobile_apps_portfolio, name='mobile_apps_portfolio'),
]
