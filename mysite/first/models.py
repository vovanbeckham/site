from django.db import models
from django.urls import reverse


class Threads(models.Model):
    thread_name = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    id_user = models.IntegerField(default=0)
    m_max = models.IntegerField(default=0)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.thread_name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.id})


class Message(models.Model):
    parent = models.ForeignKey('Threads', on_delete=models.PROTECT)
    user_id = models.IntegerField(default=0)
    message = models.TextField(blank=True)
    syga = models.BooleanField(default=False)
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse('post2', kwargs={'post_id': self.id_user})
