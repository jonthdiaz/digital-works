# Only works in local

from django.conf import settings


def send_debug_to_template(request):
    return {'DEBUG': settings.DEBUG}
