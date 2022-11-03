from machines.models.machine import Machine
from machines.models.machine_group import MachineGroup
import factory
from users.models import User
from departments.models import Department


class MachineGroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MachineGroup

    name = factory.Sequence(lambda n: f"group_{n}")


class DepartmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Department

    name = factory.Sequence(lambda n: f"department_{n}")


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"test{n}")
    password = factory.PostGenerationMethodCall("set_password", "zaq1@WSX")
    department = factory.SubFactory(DepartmentFactory)
    group = ("production",)
    email = ("testemail@gmail.com",)
    first_name = ("Test",)
    last_name = ("Test",)
    function = ("electrican",)
    mobile = ("777",)


class MachineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Machine

    factory_number = "test"
    machine_group = factory.SubFactory(MachineGroupFactory)
    name = "test"
    number = "test"
    producer = "test"
    department = factory.SubFactory(DepartmentFactory)
    machine_status = "available"
