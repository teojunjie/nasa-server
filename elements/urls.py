from django.conf.urls import url
from .views import (
    PopulateElements,
    ListPeriodicElements,
    GetPeriodicElement,
)

EXTERNAL_URL_PREFIX = 'external/v1'

urlpatterns = [
    url(r'^{url_prefix}/elements/populate?$'.format(
        url_prefix=EXTERNAL_URL_PREFIX,
    ), PopulateElements.as_view(), name='external_populate_elements'),

    url(r'^{url_prefix}/elements/list?$'.format(
        url_prefix=EXTERNAL_URL_PREFIX,
    ), ListPeriodicElements.as_view(), name='external_list_elements'),

    url(r'^{url_prefix}/elements/(?P<element_name>[^/]+)/get?$'.format(
        url_prefix=EXTERNAL_URL_PREFIX,
    ), GetPeriodicElement.as_view(), name='external_list_elements'),


]