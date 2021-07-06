from django.urls import path
from .views import article_list, article_detail, ArticleAPIView, ArticleDetail

urlpatterns = [
    # path('articles/', article_list, name='article_list'),
    # path('articles/<int:pk>/', article_detail, name='article_detail'),
    path('articles/', ArticleAPIView.as_view(), name='article_list'),
    path('articles/<int:id>/', ArticleDetail.as_view(), name='article_detail'),
    
]