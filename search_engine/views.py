from django.shortcuts import render, redirect
from django.db.models import Count
from django.http import HttpResponse, Http404
from django.forms import formset_factory
from .models import *
from .forms import SearchEntries

def home(request):
	return render(request, 'search_engine/home.html')

# Articles to genes
# -----------------

def article_search(request):
	ArticlesFormset = formset_factory(SearchEntries, extra=0)
	return render(request, 'search_engine/article-search.html', {
		'article_suggestions': Article.objects.filter(snps__gt=3).distinct()[:10],
		'articles_formset': ArticlesFormset(initial = [
			{ 'search_id': request.POST.get('search_id', '25000179') }
		]),
	})


def article_searching(request):
	if request.method == 'POST':
		return redirect('article_results', search_query=','.join(request.POST.getlist('search_id', [])))
	else:
		return redirect('article_search')


def article_results(request, search_query):
	search_ids = search_query.split(',')
	gene_results = Gene.objects.filter(snp__article__id__in=search_ids) \
								.distinct() \
								.annotate(num_snps=Count('snp')) \
								.annotate(num_articles=Count('snp__article', distinct=True))
	data = {
		'gene_results': gene_results,
		'meta': {
			'num_found': len(gene_results),
			'num_valid': 3,
			'num_entered': 3,
			'num_mesh': 0
		}
	}
	return render(request, 'search_engine/article-results.html', data)


def gene_detail(request, gene_id): # sample Article.objects.filter(snps_genes_id_in="10345")
	related_articles = Article.objects.filter(snps__genes__id__icontains=gene_id).distinct()
	related_snps = SNP.objects.filter(genes__id__icontains=gene_id).distinct()
	data = {
		'gene': Gene.objects.get(pk=gene_id),
		'num_articles': len(related_articles),
		'related_articles': related_articles,
		'num_snps': len(related_snps),
		'related_snps': related_snps,
	}
	return render(request, 'search_engine/article-result-detail.html', data)


# Genes to articles
# -----------------

def gene_search(request):
	GenesFormset = formset_factory(SearchEntries, extra=0)
	return render(request, 'search_engine/gene-search.html', {
		'genes_suggestions': Gene.objects.filter(snp__gt=3).distinct()[:10],
		'genes_formset': GenesFormset(initial = [
			{ 'search_id': request.POST.get('search_id', '259217') }
		]),
	})


def gene_searching(request):
	if request.method == 'POST':
		return redirect('gene_results', search_query=','.join(request.POST.getlist('search_id', [])))
	else:
		return redirect('gene_search')


def gene_results(request, search_query):
	# search_ids = search_query.split(',')
	search_ids = ["100287329", "105372612", "105377499"]
	article_results = Article.objects.filter(snps__genes__id__in=search_ids) \
									.distinct() \
									.annotate(num_snps=Count('snps')) \
									.annotate(num_genes=Count('snps__genes', distinct=True))
	data = {
		'article_results': article_results,
		'search_query': search_query,
		'meta': {
			'num_found': len(article_results),
			'num_valid': 3,
			'num_entered': 3
		}
	}
	return render(request, 'search_engine/gene-results.html', data)


def article_detail(request, search_query, article_id):
	related_snps = SNP.objects.filter(article__id__icontains=article_id).distinct()
	related_genes = Gene.objects.filter(snp__article__id__icontains=article_id).distinct()
	data = {
		'article': Article.objects.get(pk=article_id),
		'search_query': search_query,
		'num_genes': len(related_genes),
		'related_genes': related_genes,
		'num_snps': len(related_snps),
		'related_snps': related_snps,
	}
	return render(request, 'search_engine/gene-result-detail.html', data)
