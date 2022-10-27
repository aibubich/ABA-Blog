"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog_portal.views import ArticleDetailView, index as blog_index
from blog_portal.views import MainPageView, About
from panel_article.views import ArticleCreateView, ArticleUpdateView, PanelView, ArticleDeleteView
from blog_portal.views import ArticleDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', blog_index),
    path('', MainPageView.as_view(), name='main-page'),
    path('about/', About.as_view(), name="about"),
    path('articulo/', ArticleDetailView.as_view(), name='articulo'),
    path('article/create', ArticleCreateView.as_view(), name='article-create'),
    path('article/<pk>/update', ArticleUpdateView.as_view(), name ="article-update"),
    path('articles/', PanelView.as_view(), name ="articles"),
    path('article/<pk>/delete', ArticleDeleteView.as_view(), name ="article-delete"),
]
