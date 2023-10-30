# Generated by Django 3.2.5 on 2023-10-29 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_auto_20231029_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_apply_job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('website', models.URLField()),
                ('cv', models.FileField(upload_to='cv/')),
                ('coverletter', models.TextField(max_length=3000)),
                ('apply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.job', verbose_name='appl_job')),
            ],
        ),
    ]