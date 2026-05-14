import os
import sys

# Add project path
project_home = '/home/hightech/project34.quantumcoresoftware.com/ihiatlanta'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Activate virtualenv
activate_this = '/home/hightech/virtualenv/project34.quantumcoresoftware.com/ihiatlanta/3.10/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ihiatlanta.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()