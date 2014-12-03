from django.conf.urls import patterns, url

urlpatterns = patterns('home_app.views',
    url(r'^$', 'index', name="app-views-home"),
)