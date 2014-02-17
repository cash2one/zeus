from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zeus.views.home', name='home'),
    # url(r'^zeus/', include('zeus.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

#url(r'^$', 'zeus.views.home.index'),

#    url(r'^ticket/$', 'zeus.views.ticket.index'),
#    url(r'^ticket/add/$', 'zeus.views.ticket.add'),
#    url(r'^ticket/edit/(?P<id>\d+)/$', 'zeus.views.ticket.edit'),
    url(r'^index/ajax$','zeus.views.application.ajax'),   
#    url(r'^index/page1$','zeus.views.application.page1'),
    url(r'^index/$','zeus.views.application.index'),
    url(r'^index/page2/$','zeus.views.application.page2'),
    url(r'^index/page?3/$','zeus.views.application.page3'),
    url(r'^index/page?4/$','zeus.views.application.page4'),
    url(r'^index/application/$','zeus.views.application.application'),
    url(r'^index/myapplication_1/$','zeus.views.application.myapplication_1'),
    url(r'^index/resource/$','zeus.views.application.resource'),
    url(r'^index/review/$','zeus.views.application.review'),
    url(r'^index/review_2/$','zeus.views.application.review_2'),
    url(r'^index/review_3/$','zeus.views.application.review_3'),
    url(r'^index/post/$','zeus.views.application.post'),
#    url(r'^index/(?id=[^/]+)/$','zeus.views.application.review_2'),  
#    url(r'^index/review_2/$','zeus.views.application.review_2'),
)
