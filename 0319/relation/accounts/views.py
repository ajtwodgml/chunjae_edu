from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles.serializers import ArticleSerializer
from articles.models import Article
# Create your views here.

@api_view(['POST'])
def register(request):
    data = request.data
    serializer = UserSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    
@api_view(['GET'])
def my_articles(request) :
    #내가 쓴글
    user = request.user  #요청한 유저는 user다.
    articles = user.article_set.all() #나와 연관된 article들을 모두 가져다 줘   # 'model_set'

    serializer = ArticleSerializer(articles,many = True)
    return Response(serializer.data)

@api_view(['POST','DELETE'])
def bookmark_article(request, article_id):
    user= request.user
    article = Article.objects.get(id=article_id)

    user.bookmarks.add(article)
    #여기서 bookmarks는 accounts의 모델에서 왔다.
    
    if request.method == "POST":
        user = request.user
        article = Article.objects.get(id=article_id)
        user.bookmarks.add(article)

    elif request.method == "DELETE":
        user = request.user
        article = Article.objects.get(id=article_id)
        user.bookmarks.remove(article)

    return Response(status=204)

@api_view(['GET'])
def bookmarked_articles(request):
    user = request.user
    articles = user.bookmarks.all()
    # 유저가 북마크한거 전부다
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

# my_articles은 유저가 작성한것 
# bookmark_Article 유저가 북마크한것

