from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    text = models.CharField(max_length=20)
    title = models.TextField(max_length=0)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(null=True, blank=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

        def __str__(self):
            return self.title
