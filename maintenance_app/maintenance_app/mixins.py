from django.contrib.auth.mixins import UserPassesTestMixin


class ManagerGroupTestMixin(UserPassesTestMixin):
    """Mixin class to determine if request.user belongs to manager group"""

    def test_func(self) -> bool:
        return self.request.user.group == "manager" or self.request.user.is_superuser


class ManagerMaintenanceGroupTestMixin(UserPassesTestMixin):
    """Mixin class to determine if request.user belongs to manager OR maintenance group"""

    def test_func(self) -> bool:
        return self.request.user.group in ["manager", "maintenance"]
