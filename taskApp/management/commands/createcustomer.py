from django.core.management.base import BaseCommand, CommandError
from taskApp.models import *
class Command(BaseCommand):
    help = 'command for creating DummyCustomersData'

    #def add_arguments(self, parser):
        #parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        for i in range(10):
            user.objects.create(name="user"+str(i),IDD="user"+str(i),timezone="in/bangalore") 
        return 'customer created'
        