from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template
from django.views.generic import list_detail
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^css/(?P<path>.*)$','django.views.static.serve',
        { 'document_root': 'D:/peter/mysite/static/css/'}
    ),
    (r'^js/(?P<path>.*)$', 'django.views.static.serve',
        { 'document_root': 'D:/peter/mysite/static/js/'}
    ),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    # (r'^$', 'views.index'),
    # (r'^about/$', direct_to_template, {
    #     'template': 'about.html'
    #     }),
)
#index
urlpatterns += patterns('mysite.views',
    (r'^$', 'index'),
    (r'^admin/', include(admin.site.urls)),
)
# register and login
urlpatterns += patterns('users.views',
    (r'^user/login/$', 'login'),
    (r'^user/register/$', 'register'),  #register
    (r'^user/$', 'user_view'),
    (r'^user/logout$', 'logout'),
)