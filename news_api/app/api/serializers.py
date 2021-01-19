from rest_framework import serializers
from .models import News


class BaseChangeSerializer:
    @staticmethod
    def check_for_not_legal_fields(available_fields, fields):
        for field in fields:
            if field not in available_fields:
                raise serializers.ValidationError(f'field {field} is not registered.')


class NewsPostSerializer(serializers.ModelSerializer, BaseChangeSerializer):
    class Meta:
        model = News
        fields = ['id', 'author', 'text']

    def validate(self, data):
        self.check_for_not_legal_fields(available_fields=self.Meta.fields, fields=self.initial_data)
        return data


class NewsGetSerializer(serializers.ModelSerializer):
    creation_date = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")

    class Meta:
        model = News
        fields = ['id', 'author', 'creation_date', 'text']


class NewsPutSerializer(serializers.ModelSerializer, BaseChangeSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = News
        fields = ['id', 'author', 'text']
        extra_kwargs = {'author': {'required': False}, 'text': {'required': False}}
        read_only_fields = ['id']

    def validate(self, data):
        if (data.get('text') is not None) or (data.get('author') is not None):
            self.check_for_not_legal_fields(available_fields=self.Meta.fields, fields=self.initial_data)
            return data
        else:
            raise serializers.ValidationError('Too few arguments. You should set author or text or both of them.')

    def update(self, instance, validated_data):
        if validated_data.get('author') is not None:
            instance.author = validated_data['author']

        if validated_data.get('text') is not None:
            instance.text = validated_data['text']

        instance.save()
        return instance


