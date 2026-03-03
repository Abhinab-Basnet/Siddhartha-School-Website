from django.urls import path
from .import views

urlpatterns = [
    path('introduction/',views.introduction, name="about_introduction"),
    path('mission/', views.mission, name='mission'),
    path('prayer/', views.prayer, name='prayer'),
    path('history/', views.history, name='history'),
    path('motto/', views.motto, name='motto'),
    path('logo/', views.logo, name='logo'),
    path('achievements/', views.achievement_categories, name='achievement_list'),
    path('achievements/<int:category_id>/', views.achievement_detail, name='achievement_detail'),
    path('admission/', views.admission_form, name='admission_form'),
]
