# Generated by Django 3.2 on 2021-06-12 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_alter_game_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
