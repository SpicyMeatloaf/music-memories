from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

app_name = 'frontend'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('music/', views.music_index, name='user_index'),
    path('music/all', views.all_index, name='all_index'),
    path('music/create/', views.MusicCreate.as_view(), name='music_create'),
    path('music/<int:pk>/update/', views.MusicUpdate.as_view(), name='music_update'),
    path('music/<int:pk>/delete/', views.MusicDelete.as_view(), name='music_delete'),
    path('music/<int:music_id>/', views.music_detail, name='detail'),
    # adds photo
    path('music/<int:music_id>/add_photo', views.add_photo, name='add_photo'),
    # adds date/way of listen
    path('music/<int:music_id>/add_listen', views.add_listen, name='add_listen'),

    path('accounts/signup/', views.signup, name='signup'),

    #adds favicon 
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),

]