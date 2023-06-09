# Generated by Django 4.1.7 on 2023-05-07 22:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_essay_users_essay_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='essays',
        ),
        migrations.RemoveField(
            model_name='essay',
            name='users',
        ),
        migrations.CreateModel(
            name='UserEssay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('essay', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.essay')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='answeressayuser',
            name='essays',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.useressay'),
        ),
        migrations.AddField(
            model_name='essay',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='essay', through='api.UserEssay', to=settings.AUTH_USER_MODEL),
        ),
    ]
