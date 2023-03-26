from django.db import models
from embed_video.fields import EmbedVideoField


class Work(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, verbose_name='изображение')
    name = models.CharField(max_length=50, verbose_name='имя')
    sub_title = models.CharField(max_length=100, verbose_name='название')
    description = models.CharField(max_length=150, verbose_name='описание')
    text = models.TextField(max_length=2500, verbose_name='текст')
    created_up = models.DateTimeField(auto_now_add=True, verbose_name='дата создание')

    def __str__(self):
        return self.name


class References(models.Model):
    video = EmbedVideoField(blank=True, null=True, verbose_name='видео')
    title = models.CharField(max_length=50, verbose_name='название')
    description = models.CharField(max_length=250, verbose_name='описание')

    def __str__(self):
        return self.title


class Contacts(models.Model):
    pass
