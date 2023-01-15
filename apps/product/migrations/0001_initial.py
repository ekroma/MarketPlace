# Generated by Django 4.1.4 on 2023-01-15 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('slug', models.SlugField(blank=True, max_length=220, primary_key=True, serialize=False, verbose_name='Slug')),
                ('image', models.ImageField(upload_to='product/image')),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]