from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^$', 'profiles.views.home_public', name='url_home_public'),
    url(r'^proyectos/$', 'profiles.views.landing_projects',
        name='url_home_projects'),
)
