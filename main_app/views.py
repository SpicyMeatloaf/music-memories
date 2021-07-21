from django.shortcuts import redirect, render
from .models import Music, Photo
from django.views.generic.edit import CreateView, DeleteView, UpdateView


import boto3
import uuid

S3_BASE_URL = 'http://s3.us-east-1.amazonaws.com/'
BUCKET = 'music-memories-p4'
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
    success_url = '/music/'

class MusicDelete(DeleteView):
    model = Music
    success_url = '/music/'

def music_detail(request, music_id):
    music = Music.objects.get(id=music_id)
    return render(request, 'music/detail.html', {'music': music})

def add_photo(request, music_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, music_id=music_id)
            photo.save()
        except Exception as error:
            print('An error occured uploading file to S3')
            print(error)
    return redirect('detail', music_id=music_id)