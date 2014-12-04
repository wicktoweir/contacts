from django.conf.urls import patterns, url

urlpatterns = patterns('profile_app.views',
   url(r'^$', 'profile', name="app-views-profile"),
)