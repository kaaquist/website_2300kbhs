from django.conf.urls import patterns, include, url
from django.contrib import admin
from website_2300kbhs.views import hello, web2300kbhsIndex, hours_ahead

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website_2300kbhs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^time/$', web2300kbhsIndex),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^$', hello),
)
