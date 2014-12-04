from django.conf.urls import patterns, url

urlpatterns = patterns('contact_app.views',
   url(r'^$', 'contact_list', name="app-views-contacts"),
)