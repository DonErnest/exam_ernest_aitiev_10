from django.contrib.auth.models import User
from django.db import models

ACCESS_PUBLIC = 'public'
ACCESS_CLOSED = 'closed'
ACCESS_PRIVATE = 'private'
ACCESS_TYPE = [(ACCESS_PUBLIC, "публичный"), (ACCESS_CLOSED, "скрытый"), (ACCESS_PRIVATE, "приватный")]


class SharedFile(models.Model):
    name = models.CharField(max_length=100, verbose_name='Подпись')
    file = models.FileField(upload_to='files/', verbose_name='Файл')
    sharing_type = models.CharField(max_length=10, choices=ACCESS_TYPE, default=ACCESS_PUBLIC, verbose_name='Тип доступа')
    user_id = models.ForeignKey(User, null=True, blank=True, related_name='files', verbose_name='Загрузивший пользователь', on_delete=models.CASCADE)
    uploaded = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    downloaded_count = models.IntegerField(default=0, verbose_name='Скачан')
    privately_accessed = models.ManyToManyField(to=User, related_name='private_files', blank=True, verbose_name='Приватный доступ')
