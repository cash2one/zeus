#/usr/bin/envpython
#coding:utf-8

import os
import sys
import django.core.handlers.wsgi

sys.path.insert(0,'/var/www/html/zeus/zeus_v2')

reload(sys)

sys.setdefaultencoding('utf8')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zeus.settings")
application = django.core.handlers.wsgi.WSGIHandler()
