from django.conf.urls import patterns, url

urlpatterns = patterns(
    'profiles.views',
    url(r'^$', 'home_public', name='url_home_public'),
    url(r'^proyectos/$', 'landing_projects', name='url_projects_es'),
    url(r'^projects/$', 'landing_projects', name='url_projects_en'),
)
