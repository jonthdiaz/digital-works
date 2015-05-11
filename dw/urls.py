from __future__ import print_function
from cms.sitemaps import CMSSitemap
from django.conf.urls import *  # NOQA
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from djrill import DjrillAdminSite

admin.site = DjrillAdminSite()

admin.autodiscover()


urlpatterns = i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': {'cmspages': CMSSitemap}}),

    # url(r'^', TemplateView.as_view(
    #     template_name='sections/home/home_public.html'),
    #     name='url_home_public'),
    url(r'^$', 'profiles.views.home_public', name='url_home_public'),
    url(r'^proyectos/$', 'profiles.views.landing_projects',
        name='url_projects_es'),
    url(r'^projects/$', 'profiles.views.landing_projects',
        name='url_projects_en'),
    url(r'^', include('cms.urls')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',  # NOQA
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ) + staticfiles_urlpatterns() + urlpatterns  # NOQA
