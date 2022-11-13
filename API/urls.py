from django.urls import include, path
from rest_framework.routers import DefaultRouter

from API.views import MachineViewSet

router = DefaultRouter()
router.register(r"machines", MachineViewSet, "machines")


urlpatterns = [path("", include(router.urls))]
