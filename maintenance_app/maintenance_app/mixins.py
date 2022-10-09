from django.contrib.auth.mixins import UserPassesTestMixin


class ManagerGroupTestMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.group == "manager"


class ManagerMaintenanceGroupTestMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.group in ["manager", "maintenance"]
