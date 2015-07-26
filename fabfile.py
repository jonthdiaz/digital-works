# -*- coding: utf-8 -*-
import time
import os
from fabric.api import local, settings, abort, run, env, sudo, put
from fabric.contrib.files import exists, get
from fabric.colors import red, green

env.project_name = 'dw'
env.hosts = ['45.55.214.123']  # ['digital-workers.co']
env.user = 'dw'
env.password = 'dw_123'


env.db_name = 'dw_db'
env.db_user = 'dw_admin'
env.db_password = 'dw_admin'
env.db_host = 'localhost'
env.db_port = ''

env.date = time.strftime('%Y%m%d%H%M%S')
os.environ['DJANGO_SETTINGS_MODULE'] = '%(project_name)s.settings' % env

env.remote_backup_file_name = '/tmp/%(db_name)s-backup-%(date)s.backup' % env
env.local_backup_file_name = '%(db_name)s-backup-%(date)s.backup' % env


def runserver(port='8012', ip='0.0.0.0'):
    local('./manage.py runserver %s:%s --settings=%s.local_settings' % (ip, port, env.project_name))


def drop_create_schema():
    drop_create_command = "echo 'DROP SCHEMA PUBLIC CASCADE; CREATE SCHEMA PUBLIC;' | PGPASSWORD=%(db_password)s ./manage.py dbshell" % env
    local(drop_create_command)


def remote_db_backup():
    # date = time.strftime('%Y%m%d%H%M%S')
    fname = '%(remote_backup_file_name)s' % env

    if exists(fname):
        run('rm "%s"' % fname)
    backup_command = 'PGPASSWORD=%(db_password)s pg_dump -U %(db_user)s -h %(db_host)s -F c %(db_name)s -f %(remote_backup_file_name)s' % env
    # backup_command = 'pg_dump -U %(db_user)s -h %(db_host)s -F c %(db_name)s -f %(remote_backup_file_name)s' % env

    run(backup_command)

    get(fname, os.path.basename(fname))
    run('rm "%s"' % fname)


def update_local_db():
    # TODO: Este comando tiene serios problemas si ya hay datos en la db local
    drop_create_schema()
    remote_db_backup()
    restore_command = 'PGPASSWORD=%(db_password)s pg_restore -U %(db_user)s -d %(db_name)s -F c -c -h %(db_host)s %(local_backup_file_name)s' % env
    i = 0
    while i < 10:
        try:
            local(restore_command)
            break
        except:
            i += 1


def update_local_media():
    # se copia las imagenes de media que son las que guarda en la db el cms
    command_copy_media = 'scp -r dw@digital-workers.co:/home/dw/webapps/digital-workers/digital-works/media .'
    local(command_copy_media)


def test(app=None, run_all=None, isolated=False):
    """Run tests"""

    print green('Running Collectstatic')
    local('./manage.py collectstatic --noinput')

    print green('Running tests')
    failed_apps = []
    if not app:
        app = 'applications profiles'
    mode = ''
    if not run_all:
        mode = '--failfast'
    if not isolated:
        try:
            result = local('./manage.py test --verbosity 2 --settings=dw.local_settings %s --noinput %s' % (mode, app), capture=False)
            if result.failed:
                failed_apps += app.strip().split(' ')
        except:
            failed_apps += app.strip().split(' ')
    else:
        for a in app.strip().split(' '):
            try:
                result = local('./manage.py test %s --noinput %s' % (mode, a), capture=False)
                if result.failed:
                    failed_apps.append(a)
            except:
                failed_apps.append(a)
    if not failed_apps:
        print green('las pruebas pasaron!')
        # return
    else:
        app_list = ', '.join(failed_apps)
        print app_list
        print red('Las pruebas fallaron!')
        abort("Las pruebas fallaron")
