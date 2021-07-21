from django.contrib import admin

# Register your models here.
from .models import Music, Listen, Photo

admin.site.register(Music)
admin.site.register(Listen)
admin.site.register(Photo)