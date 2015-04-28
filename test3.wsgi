import os
import sys
import site
import datetime

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
site.addsitedir('/srv/www/blog_env/lib/python2.7/site-packages')
sys.path.append('/srv/www/islamic-blog/mysite')

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


