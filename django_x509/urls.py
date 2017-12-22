from django.urls import re_path

from . import views

app_name = 'django_x509'
urlpatterns = [
    re_path(r'^x509/ca/(?P<pk>[^/]+).crl$', views.crl, name='crl'),
]
