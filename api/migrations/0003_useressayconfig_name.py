# Generated by Django 4.2.3 on 2023-08-14 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_customessay_customessayquestion_mathtype_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='useressayconfig',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
    ]