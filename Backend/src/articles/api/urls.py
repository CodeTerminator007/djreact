from django.urls import path
from .views import ArticleViewSet 
from .views import ArticleDetailsSet
from .views import ArticleCreateSet

urlpatterns = [
    path('', ArticleViewSet.as_view()),
    path('create/',ArticleCreateSet.as_view()),
    path('<pk>', ArticleDetailsSet.as_view())
    ]
