import pytest
from .models import Department


@pytest.mark.django_db
def test_department_create():
    Department.objects.create(name="test_department")
    assert Department.objects.count() == 1
