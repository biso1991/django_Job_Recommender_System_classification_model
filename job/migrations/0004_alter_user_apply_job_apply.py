# Generated by Django 3.2.5 on 2023-11-03 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_user_apply_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_apply_job',
            name='apply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appl_job', to='job.job'),
        ),
    ]
