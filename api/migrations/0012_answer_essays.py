# Generated by Django 4.1.2 on 2023-05-15 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_remove_answer_essays_remove_essay_users_useressay_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='essays',
            field=models.ManyToManyField(blank=True, related_name='answer', through='api.AnswerEssayUser', to='api.useressay'),
        ),
    ]
