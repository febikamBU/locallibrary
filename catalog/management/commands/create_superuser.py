from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    """
    Create a superuser if none exist
    Example:
        manage.py createsuperuser_if_none_exists --user=admin --password=changeme
    """

    def add_arguments(self, parser):
        parser.add_argument("--user", required=True)
        parser.add_argument("--password", required=True)
        parser.add_argument("--email", default="admin@serenity.com")

    def handle(self, *args, **options):
        super_user = get_user_model()

        try:
            if super_user.objects.exists():
                return f'The username ({options["user"]}) already exist...'

            username = options["user"]
            password = options["password"]
            email = options["email"]

            super_user.objects.create_superuser(username=username, password=password, email=email)

            self.stdout.write(f'Local super user "{username}" was created')
        except Exception as e:
            print(e)



