from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
def create(request) :
    article = Article(title = '안녕,', content ='희승')
    article.save()
    return HttpResponse(article)
def read(request):
    articles =Article.objects.all()
    return HttpResponse(articles)
def read_id(request, id) :
    article = Article.objects.get(id=id)
    return HttpResponse(article)
@api_view(['GET','POST'])
def article_list(request) :
    if request.method == 'GET' :
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
    


@api_view(['GET','PUT','DELETE'])
def article_detail(request, id) :
    if request.method == 'GET' :
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'PUT' :
        article = Article.objects.get(id=id) # 어떤 게시글을 수정할지
        data = request.data # 어떤 내용으로 수정할지

        serializer = ArticleSerializer(article, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        article = Article.objects.get(id=id)
        article.delete()
        return Response(status=204) #no content


    