from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View
from .models import *
from .forms import *
from django.core.paginator import Paginator
from django.db.models import Q
from django.forms.formsets import formset_factory

#quontity_news = 10

def news_list(request):
	quontity_news =1
	q_n = request.GET.get('rad', None)
	
	search_query = request.GET.get('search', '')
	if search_query:
		news = News.objects.filter(Q(title__icontains = search_query) | Q(body__icontains=search_query))
	else:
		news = News.objects.all()
		
	if 'quon_news' not in request.session:
		request.session['quon_news'] = 10

	if q_n is not None:
		request.session['quon_news'] = q_n
	paginator = Paginator(news,request.session['quon_news'])
	page_number = request.GET.get('page',1)
	page = paginator.get_page(page_number)
	is_paginated = page.has_other_pages()
	if page.has_previous():
		prev_url = '?page={}'.format(page.previous_page_number())
	else:
		prev_url = ''
	if page.has_next():
		next_url = '?page={}'.format(page.next_page_number())
	else:
		next_url = ''
	context = {
	'news': page,
	'is_paginated': is_paginated,
	'next_url': next_url,
	'prev_url': prev_url,
	}
	return render(request,'news/news_list.html', context = context)

def news_detail(request, id):
	n = News.objects.get(id__iexact=id)
	return render(request,'news/news.html',context = {'n':n})

class NewsAdd(View):
	def get(self,request):
		formNews = NewsForm()
		formImages = formset_factory(ImagesForm, extra=3,
												 min_num=1, validate_min=True)
		return render(request,'news/add_news.html', context = {'formNews':formNews,'formImages':formImages})
	def post(self, request):
		formImages = formset_factory(ImagesForm, extra=3,
												 min_num=1, validate_min=True)
		newsForm = NewsForm(request.POST)
	
		imgFormSet = formImages(request.POST or None, request.FILES or None)
		if len(request.FILES)!=0:
			if (newsForm.is_valid() and imgFormSet.is_valid()):
				news = newsForm.save()
				for inline_form in imgFormSet:
					if inline_form.cleaned_data:
						img = inline_form.save(commit=False)
						img.id_news = news
						img.save()
				return redirect(news_list)
		else:
			if newsForm.is_valid():
				news = newsForm.save()
				return redirect(news_list)
		return render(request,'news/add_news.html', context = {'formNews':newsForm,'formImages':imgFormSet})

