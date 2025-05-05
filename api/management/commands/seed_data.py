from django.core.management.base import BaseCommand
from api.models import Task

class Command(BaseCommand):
    help = 'Seeds the database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Checking if data needs to be seeded...')
        
        # Only seed if no tasks exist
        if Task.objects.count() == 0:
            self.stdout.write('No tasks found. Seeding data...')
            
            # Create some sample tasks
            tasks = [
                Task(title='Complete Django REST API project', description='Create a fully functional REST API with Django.', completed=False),
                Task(title='Write tests for the API', description='Ensure the API is properly tested.', completed=False),
                Task(title='Document the API', description='Create comprehensive documentation for the API.', completed=False),
                Task(title='Set up CI/CD pipeline', description='Configure continuous integration and deployment.', completed=False),
                Task(title='Deploy the API', description='Deploy the API to a production environment.', completed=True),
            ]
            
            Task.objects.bulk_create(tasks)
            
            self.stdout.write(self.style.SUCCESS(f'Successfully seeded {len(tasks)} tasks'))
        else:
            self.stdout.write(self.style.SUCCESS('Data already exists, skipping seed operation')) 