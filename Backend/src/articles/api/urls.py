from django.urls import path
from .views import ArticleViewSet 
from .views import ArticleDetailsSet

urlpatterns = [
    path('', ArticleViewSet.as_view()),
    path('<pk>', ArticleDetailsSet.as_view())
    ]
