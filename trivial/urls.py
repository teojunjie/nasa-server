from django.conf.urls import url
from trivial.views import (
    BuildNasaTrivial,
    ListNasaTrivial,
)

EXTERNAL_URL_PREFIX = 'external/v1'

urlpatterns = [
    url(r'^{url_prefix}/trivial/build?$'.format(
        url_prefix=EXTERNAL_URL_PREFIX,
    ), BuildNasaTrivial.as_view(), name='external_trivial_build'),

    url(r'^{url_prefix}/trivial/list?$'.format(
        url_prefix=EXTERNAL_URL_PREFIX,
    ), ListNasaTrivial.as_view(), name='external_trivial_list'),

]