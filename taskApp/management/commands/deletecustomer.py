from django.core.management.base import BaseCommand, CommandError
from taskApp.models import *
class Command(BaseCommand):
    help = 'command for creating DummyCustomersData'

    #def add_arguments(self, parser):
        #parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        user.objects.all().delete() 
        return ' all customer deleted successfully'
        