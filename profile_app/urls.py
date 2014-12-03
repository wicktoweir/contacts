from django.conf.urls import patterns, url

urlpatterns = patterns('profile_app.views',
   url(r'^$', 'index', name="app-views-profile"),
)