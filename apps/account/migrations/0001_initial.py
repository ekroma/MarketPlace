# Generated by Django 4.1.4 on 2023-01-27 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('adress', models.CharField(blank=True, max_length=200)),
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Username')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('activation_code', models.CharField(blank=True, max_length=8)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
