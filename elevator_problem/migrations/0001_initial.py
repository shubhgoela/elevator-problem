# Generated by Django 4.2.4 on 2023-08-08 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Elevator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('door_status', models.CharField(choices=[('open', 'Open'), ('close', 'Close')], default='close', max_length=5)),
                ('max_floor', models.IntegerField(default=5)),
                ('min_floor', models.IntegerField(default=0)),
                ('current_floor', models.IntegerField(default=1)),
                ('state', models.CharField(choices=[('up', 'Up'), ('down', 'Down'), ('stop', 'Stop')], default='stop', max_length=5)),
                ('is_operational', models.BooleanField(default=True)),
                ('is_busy', models.BooleanField(default=False)),
            ],
        ),
    ]