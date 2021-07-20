from django.shortcuts import render
from .models import Music
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def music_index(request):
    music = Music.objects.all()
    return render(request, 'music/index.html', {'music': music})

class MusicCreate(CreateView):
    model = Music
    fields = '__all__'
    success_url = '/music/'

class MusicUpdate(UpdateView):
    model = Music
    fields = ['artist', 'album', 'song', 'genre', 'comments']

class MusicDelete(DeleteView):
    model = Music
    success_url = '/music/'

def music_detail(request, music_id):
    music = Music.objects.get(id=music_id)
    return render(request, 'music/detail.html', {'music': music})