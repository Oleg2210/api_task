from django.db import models


class News(models.Model):
    id = models.IntegerField(primary_key=True)
    author = models.TextField(max_length=8, null=False)
    creation_date = models.DateTimeField(auto_now_add=True, null=False)  # add format
    text = models.TextField(max_length=2048, null=False)

# Create your models here.
