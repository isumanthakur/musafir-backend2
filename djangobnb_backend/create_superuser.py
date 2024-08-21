from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username='testadmin').exists():
    User.objects.create_superuser('testadmin', 'admintest@example.com', 'testadminpassword123')
    print('Superuser created.')
else:
    print('Superuser already exists.')
