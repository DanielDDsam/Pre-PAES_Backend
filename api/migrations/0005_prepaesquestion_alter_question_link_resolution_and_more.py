# Generated by Django 4.2.3 on 2023-09-12 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_users_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrePAESQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('custom_essay', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prePAES_question', to='api.customessay')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='CustomEssayQuestion',
        ),
        migrations.AddField(
            model_name='prepaesquestion',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prePAES_question', to='api.question'),
        ),
    ]
