from rest_framework import serializers
from ..models import Article, Comment
from .user import UserSerializer


class ArticleListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class CommentSerializer(serializers.ModelSerializer):
        user = UserSerializer(read_only=True)

        class Meta:
            model = Comment
            fields = ('user', 'content', 'created_at', 'updated_at')
    comments = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'