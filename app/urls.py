from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('deduct/', views.deduct, name='deduct'),
    path('success/<str:args>/', views.success, name='success')
]
