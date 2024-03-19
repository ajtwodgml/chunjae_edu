from django.urls import path
from accounts import views

urlpatterns = [
    path('register/', views.register),
    path('me/articles/', views.my_articles),
    path('bookmark/<int:article_id>/', views.bookmark_article),
    path('bookmarked/', views.bookmarked_articles),
    
]

