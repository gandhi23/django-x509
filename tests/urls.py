from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, re_path
from django-x509.urls import django_x509

admin.autodiscover()

urlpatterns = [
    re_path(r'^', include('django_x509.urls', namespace='x509')),
    re_path(r'^admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
