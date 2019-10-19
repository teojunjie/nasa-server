from django.conf.urls import url
from .views import PopulateElements

EXTERNAL_URL_PREFIX = 'external/v1'

urlpatterns = [
    url(r'^{url_prefix}/elements/populate?$'.format(
        url_prefix=EXTERNAL_URL_PREFIX,
    ), PopulateElements.as_view(), name='external_populate_list'),

]