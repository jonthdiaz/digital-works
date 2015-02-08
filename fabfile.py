# -*- coding: utf-8 -*-
import time
import os
from fabric.api import local, settings, abort, run, env, sudo, put

env.project_name = 'dw'
# env.hosts = ['74.207.231.241']  # ['tutorya.monoku.com']
env.user = 'dw_admin'
env.password = 'dw_admin'

env.date = time.strftime('%Y%m%d%H%M%S')
os.environ['DJANGO_SETTINGS_MODULE'] = '%(project_name)s.settings' % env

# env.db_name = settings.DATABASES['default']['NAME']
# env.db_user = settings.DATABASES['default']['USER']
# env.db_password = settings.DATABASES['default']['PASSWORD']
# env.db_host = settings.DATABASES['default']['HOST']
# env.db_port = settings.DATABASES['default']['PORT']
# env.remote_backup_file_name = '/tmp/%(db_name)s-backup-%(date)s.backup' % env
# env.local_backup_file_name = '%(db_name)s-backup-%(date)s.backup' % env


def runserver(port='8012', ip='0.0.0.0'):
    local('./manage.py runserver %s:%s --settings=%s.local_settings' % (ip, port, env.project_name))