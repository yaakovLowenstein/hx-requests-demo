from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from faker import Faker

User = get_user_model()
fake = Faker()


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Fetch users from the API

        # Delete all users
        User.objects.all().delete()

        users = []

        for i in range(300):
            users.append(
                User(
                    id=i,
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    email=fake.email(),
                    username=fake.user_name(),
                )
            )

        User.objects.bulk_create(users)
        self.stdout.write(self.style.SUCCESS("Users refreshed successfully"))
