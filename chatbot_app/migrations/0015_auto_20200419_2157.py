# Generated by Django 2.2.5 on 2020-04-19 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot_app', '0014_feedbacklist_chat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbacklist',
            name='chat_ID',
            field=models.CharField(max_length=100),
        ),
    ]