from django.shortcuts import render
from django.http import HttpResponse

from .models import Article
from .serializers import ArticleSerializer, CommentSerializer, Comment

from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.serializers import UserSerializer

import logging

logger = logging.getLogger(__name__)


@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        # articles = Article.objects.filter(title='제목이야')
        serializer = ArticleSerializer(articles, many=True)

        logger.info("articles")
        return Response(serializer.data)
    
    elif request.method == 'POST':
        user = request.user
        data1 = request.data
        serializer = ArticleSerializer(data=data1) #Articleserializer field의 data

    

        if serializer.is_valid(raise_exception=True):
            serializer.save(author=user)
            return Response(serializer.data, status=201)





@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, id):
    if request.method == 'GET':
        article = Article.objects.get(id=id)  #Article 모델의 field에 있는 ID와 : url에 <int : id>라고 적은 ID
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        article = Article.objects.get(id=id) # 어떤 게시글을 수정할지
        data = request.data # 어떤 내용으로 수정할지

        serializer = ArticleSerializer(article, data=data)
        # serializer = ArticleSerializer(article, data=data, partial=True)  # 부분 수정

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article = Article.objects.get(id=id)
        article.delete()
        return Response(status=204) # no content
    

@api_view(['POST'])
def comment_list(request, id) :
    data = request.data
    article = Article.objects.get(id=id)  
    serializer = CommentSerializer(data=data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article) #article도 세이브해서 넣어줘
        return Response(serializer.data)
    
@api_view(["PUT", "DELETE"])
def comment_detail(request, article_pk, comment_pk):
    if request.method == "PUT":
        comment = Comment.objects.get(pk=comment_pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method =="DELETE":
        return Response(status=204)
    
@api_view(['GET'])
def bookmarked_user_list(request, article_id) :
    article = Article.objects.get(id=article_id)
    users = article.bookmark_users.all()

    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)