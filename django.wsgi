import os, sys  
from django.core.wsgi import get_wsgi_application

sys.path.append('C:/Users/joodo/Desktop/personal')  
os.environ['DJANGO_SETTINGS_MODULE'] = 'personal.settings'

application = get_wsgi_application()