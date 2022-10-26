from django.urls import path
from django.contrib import admin
from django.urls import path
from blog_portal.views import ArticleDetailView, index as blog_index
from blog_portal.views import MainPageView, About
from panel_article.views import ArticleCreateView, ArticleUpdateView
from blog_portal.views import ArticleDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', blog_index),
    path('', MainPageView.as_view(), name='main-page'),
    path('about/', About.as_view(), name="about"),
    path('articulo/', ArticleDetailView.as_view(), name='articulo'),
    path('article/create', ArticleCreateView.as_view(), name='article-create'),
    path('article/<pk>/update', ArticleUpdateView.as_view(), name ="article-update"),
]
