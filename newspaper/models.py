from django.db import models
from django.shortcuts import reverse

class News(models.Model):
	title = models.CharField(max_length=150, db_index=True)
	body = models.TextField(db_index=True)
	date_pub = models.DateTimeField(auto_now_add=True)
	def get_absolute_url(self):
		return reverse('news_detail_url', kwargs={'id':self.id})
	class Meta:
		ordering = ['-date_pub']


class Images(models.Model):
	id_news = models.ForeignKey('News', on_delete = models.CASCADE)
	pic = models.ImageField(upload_to='images/')
