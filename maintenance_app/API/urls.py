from django.urls import path, include
from API.views import MachineViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"machines", MachineViewSet, "machines")


urlpatterns = [path("", include(router.urls))]
