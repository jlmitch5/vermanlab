from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'mysite.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^upload/', include('upload.urls', namespace="upload")),
    url(r'^api/', include('api.urls')),
    url(r'^pci_ids/', include('pci_ids.urls', namespace="pci_ids")),
    url(r'^diff/', include('diff.urls', namespace="diff")),
    url(r'^cert/', include('cert.urls', namespace="cert")),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
