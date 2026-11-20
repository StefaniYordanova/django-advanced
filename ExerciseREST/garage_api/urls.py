from django.urls import path, include
from . import views

urlpatterns = [
    path('cars/', include([
        path('', views.ListCreateAPICarView.as_view()),         # list (GET) + create (POST)
        path('<int:pk>/', views.DetailAPICarView.as_view()),    # detail (GET) + update (PUT/PATCH) + delete (DELETE)
        path('stats/', views.CarStatsAPIView.as_view()),        # gives overall car statistics
    ])),
    path('manufacturers/', include([
        path('', views.ListCreateAPIManufacturerView.as_view()),        # list + create
        path('<int:pk>/', views.DetailAPIManufacturerView.as_view()),   # detail + update + delete
    ])),
]