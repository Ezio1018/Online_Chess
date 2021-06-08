# Generated by Django 3.2 on 2021-06-08 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_id', models.CharField(max_length=50, verbose_name='id')),
                ('opponent_id', models.CharField(max_length=50, verbose_name='id')),
                ('owner_side', models.CharField(default='white', max_length=10)),
                ('owner_online', models.BooleanField(default=False)),
                ('opponent_online', models.BooleanField(default=False)),
                ('fen', models.CharField(blank=True, max_length=92, null=True)),
                ('pgn', models.TextField(blank=True, null=True)),
                ('winner', models.CharField(max_length=50, verbose_name='id')),
                ('status', models.IntegerField(choices=[(1, 'Game Created. Waiting for opponent'), (2, 'Game Started'), (3, 'Game Ended')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50, unique=True, verbose_name='id')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('gender', models.CharField(choices=[('m', '男'), ('f', '女')], default='m', max_length=10, verbose_name='性别')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='邮箱')),
                ('password', models.CharField(max_length=30, verbose_name='密码')),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'User',
                'ordering': ['c_time'],
            },
        ),
    ]