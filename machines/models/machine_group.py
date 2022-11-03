from django.db import models


class MachineGroup(models.Model):
    name = models.CharField(max_length=100, help_text="Machine group")

    def __str__(self):
        return self.name
