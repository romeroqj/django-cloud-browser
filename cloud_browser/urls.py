"""Cloud browser URLs."""
from django.conf.urls import url
from django.views.generic.base import RedirectView

from cloud_browser import views
from cloud_browser.app_settings import settings


# pylint: disable=invalid-name
urlpatterns = [
    url(r'^$',
        # pylint: disable=no-value-for-parameter
        RedirectView.as_view(url='browser'),
        name="cloud_browser_index"),
    url(r'^browser/(?P<path>.*)$', views.browser, name="cloud_browser_browser"),
    url(r'^document/(?P<path>.*)$', views.document, name="cloud_browser_document"),
]

if settings.app_media_url is None:
    # Use a static serve.
    urlpatterns += [
        url(r'^app_media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.app_media_doc_root},
            name="cloud_browser_media"),
    ]
