from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.ice_cream_detail),
    path('', views.ice_cream_list),
]