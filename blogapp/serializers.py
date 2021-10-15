
from rest_framework import serializers
from rest_framework.utils import field_mapping
from .models import BlogArticle

class BlogArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogArticle
        fields = ['id','author','title','content','date']

