from django.db import models


class Department(models.Model):
    name: str = models.CharField(max_length=32, help_text="Department name")

    def __str__(self):
        return self.name
