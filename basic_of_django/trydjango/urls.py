"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from pages.views import home_view,about
from products.views import product_detail_view,product_create_view,dynamic,delete_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view,name="home"),
    path('about/', about,name="about"),
    path('create/', product_create_view,name="create"),
    path('product/', product_detail_view,name="detail"),
    path('prod/<int:my_id>/', dynamic,name="detail2"),
    path('delete/<int:my_id>/',delete_view,name="detail2")
]