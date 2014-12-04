from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'contatcts_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('home_app.urls')),
    url(r'^profile/', include('profile_app.urls')),
    url(r'^contacts/', include('contact_app.urls')),
    url(r'^groups/', include('groups_app.urls')),
)
