from django.urls import path
from apple.views import *

app_name='karthik'

urlpatterns=[
    path('if/',IF,name='IF'),
    path('if else/',IF_ELSE,name='IF_ELSE'),
    path('if elif/',IF_ELIF,name='IF_ELIF'),
    path('nested if/',NESTED_IF,name='NESTED_IF'),
]