from django.db import models
from django.conf import settings


class News(models.Model):
    id = models.IntegerField(primary_key=True)
    author = models.TextField(max_length=settings.NEWS_AUTHOR_MAX_LENGTH, blank=False, null=False)
    creation_date = models.DateTimeField(auto_now_add=True, null=False)
    text = models.TextField(max_length=settings.NEWS_TEXT_MAX_LENGTH, null=False, blank=False)

# Create your models here.
