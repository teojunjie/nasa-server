from django.conf.urls import url
from trivial.views import ListNasaTrivial

EXTERNAL_URL_PREFIX = 'external/v1'

urlpatterns = [
    url(r'^{url_prefix}/nasa/trivial/list?$'.format(
        url_prefix=EXTERNAL_URL_PREFIX,
    ), ListNasaTrivial.as_view(), name='external_nasa_trivial')
]