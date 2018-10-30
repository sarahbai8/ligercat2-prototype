from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # articles to genes
    path('articles/search', views.article_search, name='article_search'),
    path('articles/results', views.article_searching, name='article_searching'),
    path('articles/results/<str:search_query>', views.article_results, name='article_results'),
    path('articles/results/genes/<str:gene_id>', views.gene_detail, name='gene_detail'),

    # genes to articles
    path('genes/search', views.gene_search, name='gene_search'),
    path('genes/results', views.gene_searching, name='gene_searching'),
    path('genes/results/<str:search_query>', views.gene_results, name='gene_results'),
    path('genes/results/<str:search_query>/articles/<str:article_id>', views.article_detail, name='article_detail'),
]
