import json
import re
from django.db.models import manager
# from django.shortcuts import render
from django.http import response
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from .serializers import BlogArticleSerializer
from .models import BlogArticle
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView



class Root(APIView):
    def get(self, request):
        return Response("Up and running. Visit http://localhost.com:3000")

class Blogs(APIView):
    def get(self,request):
        try:
            blogs = BlogArticle.objects.all()
            serializer = BlogArticleSerializer(blogs,many=True)
            return Response(serializer.data)
        except BlogArticle.DoesNotExist:
            return Response({'Error':'No blog posts found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self,request):
        serializer = BlogArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogDetails(APIView):
    def get_blog(self,id):
        try:
            blog = BlogArticle.objects.get(id=id)
            print(blog)
            return blog
        except BlogArticle.DoesNotExist:
            return None

    def get(self, request, id):
        blog = self.get_blog(id)
        if blog:
            serializer = BlogArticleSerializer(blog)
            return Response(serializer.data)
        return Response({'Error :': f'Could not find the specific blog with id : {id}'}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self,request,id):
        blog = self.get_blog(id)
        if blog:
            serializer = BlogArticleSerializer(blog, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(request.data, status=status.HTTP_200_OK)
            return response({'Error : ':'Invalid data provided'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'Error :': f'Could not find the specific blog with id : {id}'}, status=status.HTTP_404_NOT_FOUND)


    def delete(self,request,id):
        blog = self.get_blog(id)
        if blog:
            blog.delete()
            Response({'Status:':'Deleted article with id {id}'}, status=status.HTTP_200_OK)
        return Response({'Error :': f'Could not find the specific blog with id : {id}'}, status=status.HTTP_404_NOT_FOUND)