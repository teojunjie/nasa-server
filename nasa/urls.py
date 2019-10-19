from django.conf.urls import url
from nasa.views import SaveSolarFlareView, SaveSolarBodyView

EXTERNAL_URL_PREFIX = 'external/v1'

urlpatterns = [
    url(r'^{url_prefix}/nasa/solarflare/save?$'.format(
        url_prefix=EXTERNAL_URL_PREFIX,
    ), SaveSolarFlareView.as_view(), name='external_save_solar_flare'),
    url(r'^{url_prefix}/nasa/solarbodies/save?$'.format(
        url_prefix=EXTERNAL_URL_PREFIX,
    ), SaveSolarBodyView.as_view(), name='external_save_solar_body')
]