# Generated by Django 4.2.3 on 2023-10-23 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_userquestionstate_is_modify'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
