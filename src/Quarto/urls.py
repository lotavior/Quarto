from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Quarto.views.home', name='home'),
    # url(r'^Quarto/', include('Quarto.foo.urls')),
    (r'^$', 'agenda.view.index'),
    (r'^adiciona/$', 'agenda.views.adiciona'),
    (r'^item/(?P<nr_item>\d+)/$', 'agenda.views.item'),
    (r'^remove/(?P<nr_item>\d+)/$', 'agenda.views.remove'),
    
    (r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html' }),
    (r'^logout/$', 'django.contrib.auth.views.logout_then_login',
        {'login_url': '/login/'}),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
