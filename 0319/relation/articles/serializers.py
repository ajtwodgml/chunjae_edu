from rest_framework import serializers
from .models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "article", "content")
        extra_kwargs = {"article":{"read_only":True}}
# articlesserializer클래스에서 commentserializer class를 활용하기 때문에 순서 바꾼다.
        

# comment set안에 내용들의 id값을 보기 싫을때         
class ArticleSerializer(serializers.ModelSerializer):
    class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ("id", "content")
    # Comment_Set이 1,2,3으로 나오는데 그 내용을 숫자가 아닌 정보로 보기위해서 (데이터를 이쁘게 보기 위해서) 설정

    comment_set = CommentSerializer(many=True, required=False)

    class Meta:
        model = Article
        fields = ['id','title','content','comment_set','author']
        extra_kwargs = {"author":{"read_only":True}}
        # fields = ['title']
