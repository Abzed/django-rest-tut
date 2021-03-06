# Generated by Django 4.0.3 on 2022-03-09 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('gender', models.CharField(choices=[('Male', 'MALE'), ('Female', 'FEMALE'), ('Other', 'OTHER')], max_length=55)),
                ('location', models.CharField(max_length=55)),
                ('joined_on', models.DateTimeField(auto_now_add=True)),
                ('stack', models.CharField(choices=[('Python', 'PYTHON'), ('Java', 'JAVA')], max_length=55)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
