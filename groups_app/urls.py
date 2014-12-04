from django.conf.urls import patterns, url

urlpatterns = patterns('groups_app.views',
   url(r'^$', 'group_list', name="app-views-groups"),
)