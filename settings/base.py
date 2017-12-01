import os
if os.environ.get('DJANGO_SERVER_TYPE','dev') == 'production':
    from .production import *
else:
    from .local import *