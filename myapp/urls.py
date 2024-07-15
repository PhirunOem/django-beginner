from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = 'main'),
    path('myapp/', views.myapp, name='myapp'), 
    path('myapp/details/<int:id>', views.details, name='details'),
]