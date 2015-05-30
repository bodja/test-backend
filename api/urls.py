from django.conf.urls import include, url
from rest_framework import routers
from api.views import CustomerViewSet


router = routers.DefaultRouter()
router.register(r'users', CustomerViewSet)


urlpatterns = [
    url(r'', include(router.urls)),
]
