from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

admin.autodiscover()


app_name='x509'
urlpatterns = [
    path('admin', admin.site.urls),
    # django-x509.urlS
    path('', include('django_x509.urls', namespace='x509')),
]

urlpatterns += staticfiles_urlpatterns()
