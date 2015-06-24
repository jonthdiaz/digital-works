from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^crear-contacto/$', 'applications.views.create_contact',
        name='url_create_contact'),
)
