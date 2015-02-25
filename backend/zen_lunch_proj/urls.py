from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zen_lunch_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'zen_lunch_app.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signups$', 'zen_lunch_app.views.signups', name='signups'),
)