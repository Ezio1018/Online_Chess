# Generated by Django 3.2 on 2021-06-08 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_game_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='winner',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='id'),
        ),
    ]
