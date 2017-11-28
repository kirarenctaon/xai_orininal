import os
import sys

path='/var/www/XAICWebProject'

if path not in sys.path:
  sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'XAICWebProject.settings'

import django.core.handlers.wsgi
django.setup()
application = django.core.handlers.wsgi.WSGIHandler()


