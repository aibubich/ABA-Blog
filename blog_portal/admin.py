from django.contrib import admin

from blog_portal.models import Article, Category, Publisher

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Publisher)
