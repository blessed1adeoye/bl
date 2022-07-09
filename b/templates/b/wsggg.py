import os
import sys

path = os.path.expanduser('~/blessed1')

if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'a.settings'

from django.core.wsgi import get_wsgi_application

from django.contrib.staticfiles.handlers import StaticFilesHandler

application = StaticFilesHandler(get_wsgi_application())