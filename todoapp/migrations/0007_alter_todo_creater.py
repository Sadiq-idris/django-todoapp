# Generated by Django 4.1.1 on 2022-10-16 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0006_alter_todo_creater'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='creater',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='todos', to='todoapp.info'),
        ),
    ]
