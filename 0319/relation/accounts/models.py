from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser): #만들어놓은 유저 정보들을 활용하겠다.
    bookmarks = models.ManyToManyField("articles.Article", related_name="bookmark_users")
 # user와 aticle간의 관계설정
