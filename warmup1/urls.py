from django.conf.urls import patterns, include, url
from login.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'warmup1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'login.views.index'),
    url(r'^users/login$', 'login.views.login'),
    url(r'^users/add$', 'login.views.add'),
    url(r'^TESTAPI/resetFixture$', 'login.views.resetFixture'),
    url(r'^TESTAPI/unitTests$', 'login.views.unitTests'),
)
