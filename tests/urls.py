from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import re_path, include

admin.autodiscover()

urlpatterns = [
    re_path(r'^', include('django_x509.urls'),
    re_path(r'^admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
