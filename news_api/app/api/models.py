from django.db import models


class News(models.Model):
    id = models.IntegerField(primary_key=True)
    author = models.TextField(max_length=128, blank=False, null=False)
    creation_date = models.DateTimeField(auto_now_add=True, null=False)
    text = models.TextField(max_length=2048, null=False, blank=False)

# Create your models here.
