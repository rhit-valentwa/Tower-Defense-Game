# Generated by Django 4.1.7 on 2023-03-28 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvailablePlayer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('game_id', models.TextField()),
                ('wants_to_attack', models.BooleanField(default=True)),
            ],
        ),
    ]
