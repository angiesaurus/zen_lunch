from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^home', 'zendine.views.home', name='home'),
    url(r'', 'zendine.views.home', name='signup'),
    url(r'^admin/', include(admin.site.urls)),
)
