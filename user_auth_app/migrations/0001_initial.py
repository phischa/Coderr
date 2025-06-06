# Generated by Django 5.2.1 on 2025-05-21 14:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(blank=True, null=True, upload_to='profile-images/')),
                ('location', models.CharField(blank=True, max_length=255)),
                ('tel', models.CharField(blank=True, max_length=20)),
                ('description', models.TextField(blank=True)),
                ('working_hours', models.CharField(blank=True, max_length=255)),
                ('type', models.CharField(choices=[('business', 'Business'), ('customer', 'Customer')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_guest', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
