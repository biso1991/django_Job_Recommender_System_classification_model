# Generated by Django 4.2.5 on 2023-10-17 13:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_job_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
