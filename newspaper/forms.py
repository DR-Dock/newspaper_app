from django import forms
from django.forms import inlineformset_factory
from .models import *

class NewsForm(forms.ModelForm):
	images = forms 
	class Meta:
			model = News
			fields = ['title','body']
			widgets = {
			'title' : forms.TextInput(attrs={'class': 'form-control'}),
			'body' : forms.Textarea(attrs={'class': 'form-control'}),
			}


class ImagesForm(forms.ModelForm):
	class Meta:
		model = Images
		fields = ['pic']
		

#BookFormSet = inlineformset_factory(Author, Book, fields=('title',))
#author = Author.objects.get(name='Mike Royko')
#formset = BookFormSet(instance=author)
