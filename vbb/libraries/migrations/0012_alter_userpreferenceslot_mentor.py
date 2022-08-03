# Generated by Django 3.2.13 on 2022-08-03 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('libraries', '0011_computer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreferenceslot',
            name='mentor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='preference_mentor', to=settings.AUTH_USER_MODEL),
        ),
    ]
