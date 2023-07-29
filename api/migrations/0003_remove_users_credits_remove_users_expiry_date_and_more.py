# Generated by Django 4.1.2 on 2022-11-24 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_users_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='credits',
        ),
        migrations.RemoveField(
            model_name='users',
            name='expiry_date',
        ),
        migrations.RemoveField(
            model_name='users',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='users',
            name='linkedin_token',
        ),
        migrations.AddField(
            model_name='users',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='is_deleted',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]