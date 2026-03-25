from django.core.management.base import BaseCommand
from django.utils import timezone
from accounts.models import FamilyUser


class Command(BaseCommand):
    help = "Deactivate expired guest accounts"

    def handle(self, *args, **options):
        expired = FamilyUser.objects.filter(
            is_temporary=True, expires_at__lt=timezone.now(), is_active=True
        )
        count = expired.update(is_active=False)
        self.stdout.write(f"Deactivated {count} expired guest accounts")
