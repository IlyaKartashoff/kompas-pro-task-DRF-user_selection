from django.core.management.base import BaseCommand
from user_selection.models import User

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        data = [
            {'username': 'Baddy', 'password': '123', 'role': 'user','offer': False},
            {'username': 'June', 'password': '123','role': 'manager','offer': False},
            {'username': 'Daddy', 'password': '123','role': 'CRMadmin','offer': False},
            
        ]
        for item in data:
            user = User.objects.create(username=item['username'],
                                role=item['role'],
                                offer=item['offer'],
                                password=item['password'],
                                )
            user.save()
            print(f'{user.username} done.')
        