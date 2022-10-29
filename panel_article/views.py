from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blog_portal.models import Article, Category, Publisher
from blog_portal.views import BaseView




class PanelView(BaseView, ListView):
    
    queryset = Article.objects.all()
    template_name = "panel_article/article_list.html"    
    context_object_name = "articles"

class ArticleCreateView(CreateView):
    model = Article
    fields = ['short_content','title' , 'content', 'author','image', 'is_headline', 'image', 'date_published', 'category']
    template_name = "panel_article/article_form.html"
    success_url = reverse_lazy('articles')

class ArticleUpdateView(BaseView, UpdateView):
    model = Article
    fields = ['title', 'short_content', 'content', 'author','image', 'is_headline', 'image', 'date_published', 'category']
    template_name = "panel_article/article_form.html"
    success_url = reverse_lazy('articles')

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "panel_article/article_confirm_delete.html"
    success_url = reverse_lazy('articles')

class CategoryPanelView(BaseView, ListView):
    
    queryset = Category.objects.all()
    template_name = "panel_article/category_list.html"    
    context_object_name = "category"

class CategoryCreateView(CreateView):
    model = Category
    fields = ['name']
    template_name = "panel_article/category_form.html"
    success_url = reverse_lazy("category")

class CategoryUpdateView(BaseView, UpdateView):
    model = Category
    fields = ['name']
    template_name = "panel_article/category_form.html"
    success_url = reverse_lazy('category')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "panel_article/category_confirm_delete.html"
    success_url = reverse_lazy('category')

class SearchPostByCategory(ListView):
    def get_queryset(self):
        post_category = self.request.GET.get('post-category')
        return Article.objects.filter(category=post_category)


class PublisherPanelView(BaseView, ListView):
    queryset = Publisher.objects.all()
    template_name = "panel_article/publisher_list.html"    
    context_object_name = "publisher"

class PublisherCreateView(CreateView):
    model = Publisher
    fields = ['name','surname','country', 'age']
    template_name = "panel_article/publisher_form.html"
    success_url = reverse_lazy("publisher")

class PublisherUpdateView(BaseView, UpdateView):
    model = Publisher
    fields = ['name','surname','country', 'age']
    template_name = "panel_article/publisher_form.html"
    success_url = reverse_lazy('publisher')

class PublisherDeleteView(DeleteView):
    model = Publisher
    template_name = "panel_article/publisher_confirm_delete.html"
    success_url = reverse_lazy('publisher')