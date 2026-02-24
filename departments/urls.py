from django.urls import path
from . import views

urlpatterns = [
    path('', views.department_list, name='dept_list'),
    path('<slug:slug>/', views.department_detail, name='dept_detail'),
]