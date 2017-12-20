from django.conf.urls import url ,include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()


urlpatterns = [
    url(r'^admin', admin.site.urls),
    # django-x509.urlS
    url(r'^', include('django_x509.urls')),
]

urlpatterns += staticfiles_urlpatterns()
