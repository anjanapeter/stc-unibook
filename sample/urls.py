"""
URL configuration for sample project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from my_app.views import login_view
from my_app.views import faculty_home
from my_app.views import submit_form
from my_app.views import calendar
from my_app.views import available_halls
from django.shortcuts import redirect

urlpatterns = [
    path('', login_view, name='login'),
    #path('admin/', admin.site.urls),
    #path('', login_view, name='login'),
    path('faculty-home/', faculty_home, name='faculty_home'),
    path('submit-form/', submit_form, name='submit_form'),
    path('calendar/', calendar, name='calendar'),
    path('available-halls/', available_halls, name='available_halls'),
    path('submit_form/', submit_form, name='submit_form'),
    #path('book_hall/<int:hall_id>/', views.book_hall, name='book_hall')
    path('admin/', admin.site.urls),
]
#from django.urls import path

#from my_app import views
#urlpatterns = [
    #path('submit_form/', views.submit_form, name='submit_form'),
    #path('book_hall/<int:hall_id>/', views.book_hall, name='book_hall'),
#]
