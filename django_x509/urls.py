from django.urls import path

from . import views

app_name='django_x509'
urlpatterns = [
    path(r'^x509/ca/(?P<pk>[^/]+).crl$', views.crl, name='crl'),
]
