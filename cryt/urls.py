from django.conf import settings
from django.urls import path, include, re_path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('mydocs', mydocs, name='mydocs'),
    path('shared', shared, name='shared'),
    path('verify', verify, name='verify'),
    path('history', history, name='history'),
    re_path(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], protected_serve, {'document_root': settings.MEDIA_ROOT})
]