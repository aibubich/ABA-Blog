from django.shortcuts import render
from django.views.generic import ListView, TemplateView, View
from blog_portal.models import Article
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


class ArticleDetailView(TemplateView):

    template_name = "blog_portal/articulo.html"


class SearchPostByCategory(ListView):
    def get_queryset(self):
        post_category = self.request.GET.get('post-category')
        return Article.objects.filter(category=post_category)