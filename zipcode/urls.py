from django.conf.urls import patterns, include, url
from zipcode import views
from django.views.generic import TemplateView


urlpatterns = patterns('',
   url(r'^$', TemplateView.as_view(template_name="zipcode/home.html"), name="home"),
   url(r'^search/$', views.get_zip,),
   url(r'^search/(?P<postcode>\d{5})$', views.results, name='results'),
   url(r'^contact/$', views.get_contact, name="contact"),
   url(r'^thanks/$', TemplateView.as_view(template_name="thanks.html"), name="thanks"),
   url(r'^careers/$', views.get_resume, name="careers"),
)
