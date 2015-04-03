from django.conf.urls import patterns, include, url
from django.contrib import admin
from sangbok import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'snapps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home),
    url(r'^(\d+)/$', views.song),
    url(r'^add/', views.addsong),
    url(r'^(\d+)/edit/$', views.editsong),
    url(r'^(\d+)/delete/$', views.deletesong),
    url(r'^list/$', views.list),
    url(r'^search/?', include('haystack.urls')),
    url(r'^random/$', views.random),
)
