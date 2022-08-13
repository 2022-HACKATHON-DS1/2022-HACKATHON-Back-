from django.contrib import admin
from django.urls import path
from . import views
from mainapp import views as mainapp_views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.login, name='login'),
    path('home/', mainapp_views.home, name='home'),

]  
    