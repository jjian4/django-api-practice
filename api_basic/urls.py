from django.urls import path, include
# from .views import article_list, article_detail
from .views import ArticleAPIView, ArticleDetailAPIView, GenericArticleAPIView, GenericArticleDetailAPIView, ArticleViewSet, GenericArticleViewSet
from rest_framework.routers import DefaultRouter


# Router for viewset
router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

# Router for generic viewset
router2 = DefaultRouter()
router2.register('article', GenericArticleViewSet, basename='article')


urlpatterns = [

    # GENERIC VIEWSETS
    path('genviewset/', include(router2.urls)),

    # VIEWSETS: handles both articles and article detail
    path('viewset/', include(router.urls)),

    # GENERIC VIEWS
    path('generic/article/', GenericArticleAPIView.as_view()),
    path('generic/article/<int:id>', GenericArticleDetailAPIView.as_view()),

    # CLASS BASED VIEWS
    path('article/', ArticleAPIView.as_view()),
    path('article/<int:id>/', ArticleDetailAPIView.as_view()),

    # FUNCTION BASED VIEWS (look at views.py)
    # path('article/', article_list),
    # path('article/<int:pk>/', article_detail),

]
