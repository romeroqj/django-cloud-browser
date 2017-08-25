# pylint: disable=no-value-for-parameter

from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.static import serve

# Enable admin.
admin.autodiscover()

ADMIN_URLS = False
urlpatterns = []  # pylint: disable=C0103

if ADMIN_URLS:
    urlpatterns += [
        # Admin URLs. Note: Include ``urls_admin`` **before** admin.
        url(r'^$', RedirectView.as_view(url='/admin/'), name='index'),
        url(r'^admin/cb/', include('cloud_browser.urls_admin')),
    ]

else:
    urlpatterns += [
        # Normal URLs.
        url(r'^$', RedirectView.as_view(url='/cb/'), name='index'),
        url(r'^cb/', include('cloud_browser.urls')),
    ]

urlpatterns += [
    # Hack in the bare minimum to get accounts support.
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/$', RedirectView.as_view(url='/login/')),
    url(r'^accounts/profile', RedirectView.as_view(url='/')),
]

if settings.DEBUG:
    # Serve up static media.
    urlpatterns += [
        url(r'^' + settings.MEDIA_URL.strip('/') + '/(?P<path>.*)$',
            serve, {'document_root': settings.MEDIA_ROOT}),
    ]
