from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()


urlpatterns = [
    url(r'^', 'django_x509.urls', name='x509')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
