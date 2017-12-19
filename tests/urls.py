from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # django-x509 urls
    # keep the namespace argument unchanged
    url(r'^x509/', include('django_x509.urls')),
]

urlpatterns += staticfiles_urlpatterns()
