from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from blog_portal.models import Article
from blog_portal.views import BaseView


#class PanelView(LoginRequiredMixin, BaseView, ListView):

class PanelView(BaseView, ListView):
    
    queryset = Article.objects.all()
    template_name = "panel_article/article_list.html"    
    context_object_name = "articles"

#class ArticleCreateView(LoginRequiredMixin, CreateView):

class ArticleCreateView(CreateView):
    model = Article
    fields = ['short_content','title' , 'content', 'author','image', 'is_headline', 'image', 'date_published']
    template_name = "panel_article/article_form.html"
    success_url = reverse_lazy("main-page")


#    class ArticleUpdateView(LoginRequiredMixin, BaseView, UpdateView):

class ArticleUpdateView(BaseView, UpdateView):
    model = Article
    fields = ['title', 'short_content', 'content', 'author','image', 'is_headline', 'image', 'date_published']
    success_url = reverse_lazy('main-page')
