"""
WSGI config for Using_Conditional_Statements_in_HTML_pages project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Using_Conditional_Statements_in_HTML_pages.settings')

application = get_wsgi_application()
