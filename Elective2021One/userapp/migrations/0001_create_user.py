from django.db import migrations, models

def load_default_user(apps, schema_editor):
    User = apps.get_model(app_label='auth', model_name='User')
    
    #iam@rideon
    password = 'pbkdf2_sha256$216000$ON9ejvp5nYkB$liA8tb0zMajrTIL5EoEnsTYFqpZZZfqN6MNEXsxAds0='
    
    user1 = User(id=1,first_name="Super",last_name="Admin",username='superadmin',password=password,email='superadmin@gmail.com')
    user1.save()


class Migration(migrations.Migration):
    #dependencies = [
    #    ('nldbaseapp', '0001_initial'),
    #]
    operations = [
        migrations.RunPython(load_default_user)
    ]