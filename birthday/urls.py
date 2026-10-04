from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('story/', views.story, name='story'),
    path('memories/', views.memories, name='memories'),
    path('reasons/', views.reasons, name='reasons'),
    path('birthday/', views.birthday, name='birthday'),
]