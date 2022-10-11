import pytest
from .models import User
from departments.models import Department


@pytest.mark.django_db
def test_user_create():
    department = Department.objects.create(name="test")
    User.objects.create(username="username", department=department)
    assert User.objects.count() == 1
