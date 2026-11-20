from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.ListCreateAPICarView.as_view()),           # list (GET) + create (POST)
    path('cars/<int:pk>/', views.DetailAPICarView.as_view()),       # detail (GET) + update (PUT/PATCH) + delete (DELETE)
    path('manufacturers/', views.ListCreateAPIManufacturerView.as_view()),       # list + create
    path('manufacturers/<int:pk>/', views.DetailAPIManufacturerView.as_view()),  # detail + update + delete
]