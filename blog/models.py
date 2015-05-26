from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	created = models.DateTimeField()
	imag = models.ImageField(upload_to='pics', blank=True,default='')
	
	def __unicode__(self):
		return self.title

