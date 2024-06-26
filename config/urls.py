"""board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import config.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('', views.index),
#로그인
    path('signup/', views.signup),
    path('signin/', views.signin),
    path('signout/', views.signout),
#게시판
    path('article/write/', views.write),
    path('article/list/', views.list),
    path('article/detail/<int:id>/', views.detail),
    path('article/update/<int:id>/', views.update),
    path('article/delete/<int:id>/', views.delete),
#지도
    path('map/', views.map),
    path('map_data/', views.map_data),
    path('map_data2/', views.map_data2),
#이메일
    path('contact/', views.contact),
]
