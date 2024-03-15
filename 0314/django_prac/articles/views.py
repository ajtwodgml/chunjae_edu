from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Article
# Create your views here.
def random_data(request, num) :
    return HttpResponse(f"숫자 :{num}")

def create(request):
    article = Article(title = '제목인데용', content = '내용인데용') 
    article.save()
    return HttpResponse(article)

def read(request) : 
    article = Article.objects.all()
    return HttpResponse(article)