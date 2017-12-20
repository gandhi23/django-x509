from django.urls import include, re_path
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

app_name = 'django_x509'
urlpatterns = [
    re_path(r'^', include('django_x509.urls')),
    re_path(r'^admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
