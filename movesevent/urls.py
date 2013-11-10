from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'movesevent.views.home', name='home'),
    # url(r'^movesevent/', include('movesevent.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Grappelli
    url(r'^grappelli/', include('grappelli.urls')),
    
    # Movesevent
    url(r'^syncuser/(?P<user_id>\d+)/', 'movesevent.views.sync4user', name='syncuser'),
    url(r'^oauth_return/(?P<user_id>\d+)/', 'movesevent.views.oauth_return', name='oauth_return'),
    

)
