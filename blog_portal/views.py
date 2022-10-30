from django.shortcuts import render
from django.views.generic import ListView, TemplateView, View, DetailView
from blog_portal.models import Article, Category
from panel_article import *


def index(request):
    return render(request, 'blog_portal/index.html')

class BaseView(View):

     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['headline'] = Article.objects.filter(is_headline=True).order_by('date_updated').first()
        return context 

class MainPageView(BaseView, ListView):
    queryset = Article.objects.all()
    context_object_name = "articles"
    template_name = "blog_portal/index.html"

    def get(self, request):
        article = Article.objects.all()
        headline = {
            'tab':'ABA Blogs Inicio',
            'headline':'Bienvenido a ABA Blog!',
            'sub':'Un trabajo de Agustina, Bruno y Alvaro para Coderhouse'

        }
        return render(request, self.template_name, {'headline':headline})
    

class About(BaseView, TemplateView):

    template_name = "blog_portal/about.html"



#class ArticleDetailView(DetailView):

    #model = Article
    #context_object_name = "article"
    
    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    return contex

class ArticleDetailView(TemplateView):

    template_name = "blog_portal/articulo.html"
    
def SearchPostByCategory(request):
    qs = Article.objects.all()
    post_category = request.GET.get('post-category')
    if post_category != '' and post_category is not None:
        qs = qs.filter(category=post_category)
    context = {
        'queryset':qs
    }
    return render (request, "blog_portal/article_filter.html", context) 