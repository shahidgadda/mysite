from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView, TemplateView
from blog.models import Post

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-created")[:20],
    							template_name="index.html")),
    url(r'^book_detail/(?P<pk>\d+)$', DetailView.as_view(model=Post,
    							template_name="details.html")),
	url(r'^archives/$', ListView.as_view(queryset=Post.objects.all().order_by("-created"),
    							template_name="archives.html")),
	url(r'^photos/$', ListView.as_view(queryset=Post.objects.all().order_by("-created"),
    							template_name="photos.html")),
    url(r'^contact/', TemplateView.as_view(template_name="contact.html")),
    url(r'^thanks/', TemplateView.as_view(template_name="thanks.html")),
    url(r'^invalid/', TemplateView.as_view(template_name="invalid.html")),
	url(r'^autocomplete/', 'blog.views.autocomplete'),
    url(r'^sendMail/', 'blog.views.sendMail'),
)
