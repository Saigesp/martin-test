from django.conf.urls import url
from . import views

urlpatterns = [
    # test
    url(r'^leaflet/$', views.leaflet_test, name='leaflet-test'),
]