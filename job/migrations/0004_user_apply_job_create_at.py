# Generated by Django 3.2.5 on 2023-10-30 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_user_apply_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_apply_job',
            name='create_at',
            field=models.DateField(auto_now=True),
        ),
    ]