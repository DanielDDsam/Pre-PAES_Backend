# Generated by Django 4.2.3 on 2023-10-30 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_alter_achievement_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='avatar',
            field=models.URLField(blank=True, null=True),
        ),
    ]
