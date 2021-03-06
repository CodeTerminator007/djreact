from .serializers import ArticleSerializer
from articles.models import Article
from rest_framework.generics import ListAPIView 
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import CreateAPIView
class ArticleViewSet(ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

class ArticleDetailsSet(RetrieveAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

class ArticleCreateSet(CreateAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()    