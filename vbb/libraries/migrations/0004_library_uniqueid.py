# Generated by Django 3.2.13 on 2022-06-10 18:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0003_auto_20220608_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='uniqueID',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
