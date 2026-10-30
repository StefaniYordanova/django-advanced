from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('fbv/login', views.fbv_login, name='fbv-login'),
    path('fbv/logout', views.fbv_logout, name='fbv-logout'),
    path('register', views.register, name='register'),

]