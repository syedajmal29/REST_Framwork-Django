"""
URL configuration for django_rest_main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #web application endpoint 
    path('students/', include('students.urls')),


    #API Endpoints
    #Most Api will start from api/
    path('api/v1/', include('api.urls')),   #this will go to api folder urls.py file and then to the respective app urls.py file
    path('', include('books_review.urls')),  # Include the books_review app URLs
]
