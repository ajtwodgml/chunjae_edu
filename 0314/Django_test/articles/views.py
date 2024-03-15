from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
# def data(request):
#     return HttpResponse("게시글")
# def sleep(request):
#     return HttpResponse("식곤증...")
# def json_data(request):
#     data ={
#         'title': '제목',
#         'content' : '내용'
#     }
#     return JsonResponse(data)
# import random
# def random_data(request, num) :
#     return HttpResponse(num)
# def str_data(request, name) :
#     return HttpResponse(f"{name}:천재")

# def create(request) :
#     article = Article(
#         title = '이거 제목임',
#         content = '이건 내용임',
#     )
#     article.save()
#     return HttpResponse(article)

# def read(request) :
#     articles = Article.objects.all()
#     return HttpResponse(articles)
    
# def read_single(request, id) :
#     article = Article.objects.get(id=id)
#     return HttpResponse(article)
@api_view(['GET', 'POST'])
def article_list(request) :
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many = True)
        return Response(serializer.data)
    elif request.method == 'POST' :
        data = request.data
        serializer = ArticleSerializer(data=data)

        if serializer.is_valid(raise_exception= True):
            serializer.save()
            return Response(serializer.data, status = 201)
    
@api_view(['GET'])
def article_detail(request, id) :
    article = Article.objects.get(id=id)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)