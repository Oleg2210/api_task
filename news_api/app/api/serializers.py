from django.http import Http404
from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'author', 'creation_date', 'text']
        read_only_fields = ['creation_date']


class NewsPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'author', 'text']
        extra_kwargs = {'author': {'required': False}, 'text': {'required': False}}
        read_only_fields = ['id']
