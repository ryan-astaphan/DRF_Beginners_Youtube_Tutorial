from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    article_list, 
    article_detail, 
    ArticleAPIView, 
    ArticleDetail,
    GenericAPIView,
    ArticleViewSet
    )

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    # path('articles/', article_list, name='article_list'), # Function-based
    # path('articles/<int:pk>/', article_detail, name='article_detail'), # Function-based
    # path('articles/', ArticleAPIView.as_view(), name='article_list'), # Class-based
    # path('articles/<int:id>/', ArticleDetail.as_view(), name='article_detail'), # Class-based
    path('articles/', GenericAPIView.as_view(), name='article_list'),
    path('articles/<int:id>/', GenericAPIView.as_view(), name='article_detail'),
    path('viewset/', include(router.urls)),    
    path('viewset/<int:pk>', include(router.urls)),    
]