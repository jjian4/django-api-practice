from django.urls import path
# from .views import article_list, article_detail
from .views import ArticleAPIView, ArticleDetailAPIView, GenericArticleAPIView, GenericArticleDetailAPIView

urlpatterns = [

    # CLASS BASED VIEWS
    path('article/', ArticleAPIView.as_view()),
    path('article/<int:id>/', ArticleDetailAPIView.as_view()),

    # FUNCTION BASED VIEWS (look at views.py)
    # path('article/', article_list),
    # path('article/<int:pk>/', article_detail),

    
    # GENERIC VIEWS
    path('generic/article/', GenericArticleAPIView.as_view()),
    path('generic/article/<int:id>', GenericArticleDetailAPIView.as_view())

]
