# Generated by Django 4.1.1 on 2022-10-14 15:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_remove_todo_creater_todo_date_time_todo_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('thumbnail', models.ImageField(default='default.png', null=True, upload_to='pics')),
            ],
        ),
        migrations.RemoveField(
            model_name='todo',
            name='date_time',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='title',
        ),
        migrations.AddField(
            model_name='todo',
            name='creater',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='todoapp.info'),
        ),
    ]
