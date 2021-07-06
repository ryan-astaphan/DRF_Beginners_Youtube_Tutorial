from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.Serializer):
    author = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    title = serializers.CharField(max_length=100)
    date = serializers.DateTimeField()

    def create(self, validated_data):
        return Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.email = validated_data.get('email', instance.email)
        instance.title = validated_data.get('title', instance.title)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance