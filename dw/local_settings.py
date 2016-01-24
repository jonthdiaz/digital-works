from dw.settings import *
 
print ('Usando local_settings')
DEBUG = True
#Auth User Model Information
#AUTH_USER_MODEL = 'profiles.User'
 
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
CELERY_ALWAYS_EAGER = True
 
INTERNAL_IPS = ('127.0.0.1',)
#Debug Toolbar
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
#TEST_RUNNER = 'djcelery.contrib.test_runner.CeleryTestSuiteRunner'
 
show_debug_toolbar = False
 
if show_debug_toolbar:
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
        'HIDE_DJANGO_SQL': False,
        'TAG': 'div',
        'ENABLE_STACKTRACES': True,
    }
 
    INSTALLED_APPS += (
        'debug_toolbar',
        'jstemplate',
    )
 
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
 
TEMPLATE_CONTEXT_PROCESSORS += (
    'applications.context_processors.send_debug_to_template',
)
