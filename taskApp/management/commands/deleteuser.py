from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
class Command(BaseCommand):
    help = 'command for creating superuser'

    #def add_arguments(self, parser):
        #parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        User.objects.all().delete()
        return 'users deleted'
        