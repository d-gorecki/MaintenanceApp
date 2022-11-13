from django.core.mail import EmailMessage
from django.core.management.base import BaseCommand, CommandError
from django.db.models import QuerySet
from django.utils.timezone import datetime, now, timedelta

from maintenance.models.maintenance_schedule import MaintenanceSchedule


class Command(BaseCommand):
    """Management command to send remainder(email) of upcoming maintenances (planned_date - 1 day).
    This e-mail sending feature is established to cooperate with django-contrab package"""

    tomorrow: datetime.date = datetime.date(now()) + timedelta(1)

    def handle(self, *args, **options) -> None:
        """Check for pending maintenance schedules with planned_date day ahead of today.
        Send remainder(email) to corresponding user(servicesman)"""
        schedules: QuerySet[MaintenanceSchedule] = MaintenanceSchedule.objects.filter(
            planned_date=self.tomorrow, status="pending"
        )
        if schedules:
            for schedule in schedules:
                subject: str = (
                    f"Reminder: Tomorrow maintenance of {schedule.machine.name}."
                )
                message: str = (
                    f"Hello {schedule.user.first_name} {schedule.user.last_name},\nthis is default reminder "
                    f"of tomorrow ({self.tomorrow}) {schedule.maintenance_type.type} maintenance of {schedule.machine}.\nPlease remember to fulfill maintenance report."
                )
                recipient_list: list[str] = [schedule.user.email]
                msg: EmailMessage = EmailMessage(subject, message, to=recipient_list)
                msg.send()
