from django.conf.urls import url
from .views import (
    CreateCompoundView,
    ListCompoundsView,
)
EXTERNAL_URL_PREFIX = 'external/v1'

urlpatterns = [
    url(r'^{url_prefix}/compounds/(?P<compound_name>[^/]+)/create?$'.format(
        url_prefix=EXTERNAL_URL_PREFIX,
    ), CreateCompoundView.as_view(), name='external_compounds_create'),

    url(r'^{url_prefix}/compounds/get?$'.format(
        url_prefix=EXTERNAL_URL_PREFIX,
    ), ListCompoundsView.as_view(), name='external_compounds_get'),

]