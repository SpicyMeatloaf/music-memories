from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('music/', views.music_index, name='index'),
    path('music/create/', views.MusicCreate, name='music_create'),
    path('music/update/', views.MusicUpdate, name='music_update'),
    path('music/delete/', views.MusicDelete, name='music_delete'),
    path('music/<int:music_id>/', views.music_detail, name='detail'),

]