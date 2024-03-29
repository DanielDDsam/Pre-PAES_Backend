# Generated by Django 4.2.3 on 2023-10-14 23:05

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_question_dificult_alter_question_link_resolution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='created',
            field=api.models.DateTimeSecondsField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='updated',
            field=api.models.DateTimeSecondsField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='created',
            field=api.models.DateTimeSecondsField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='updated',
            field=api.models.DateTimeSecondsField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='answeressayuser',
            name='created',
            field=api.models.DateTimeSecondsField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='answeressayuser',
            name='updated',
            field=api.models.DateTimeSecondsField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='answerprepaes',
            name='created',
            field=api.models.DateTimeSecondsField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='answerprepaes',
            name='updated',
            field=api.models.DateTimeSecondsField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='customessay',
            name='created',
            field=api.models.DateTimeSecondsField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='customessay',
            name='updated',
            field=api.models.DateTimeSecondsField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='customessayquestion',
            name='created',
            field=api.models.DateTimeSecondsField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='customessayquestion',
            name='updated',
            field=api.models.DateTimeSecondsField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='mathtype',
            name='created',
            field=api.models.DateTimeSecondsField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='mathtype',
            name='updated',
            field=api.models.DateTimeSecondsField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='prepaes',
            name='created',
            field=api.models.DateTimeSecondsField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='prepaes',
            name='updated',
            field=api.models.DateTimeSecondsField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='prepaesquestion',
            name='created',
            field=api.models.DateTimeSecondsField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='prepaesquestion',
            name='updated',
            field=api.models.DateTimeSecondsField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='created',
            field=api.models.DateTimeSecondsField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='updated',
            field=api.models.DateTimeSecondsField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='questionerror',
            name='created',
            field=api.models.DateTimeSecondsField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='questionerror',
            name='updated',
            field=api.models.DateTimeSecondsField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='typesessaycustom',
            name='created',
            field=api.models.DateTimeSecondsField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='typesessaycustom',
            name='updated',
            field=api.models.DateTimeSecondsField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='userachievement',
            name='created',
            field=api.models.DateTimeSecondsField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='userachievement',
            name='updated',
            field=api.models.DateTimeSecondsField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='useressayconfig',
            name='created',
            field=api.models.DateTimeSecondsField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='useressayconfig',
            name='updated',
            field=api.models.DateTimeSecondsField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='useressayconfigtypes',
            name='created',
            field=api.models.DateTimeSecondsField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='useressayconfigtypes',
            name='updated',
            field=api.models.DateTimeSecondsField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='userquestionstate',
            name='created',
            field=api.models.DateTimeSecondsField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='userquestionstate',
            name='updated',
            field=api.models.DateTimeSecondsField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='created',
            field=api.models.DateTimeSecondsField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='updated',
            field=api.models.DateTimeSecondsField(auto_now=True, null=True),
        ),
    ]
