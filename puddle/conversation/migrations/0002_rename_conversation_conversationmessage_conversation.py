# Generated by Django 4.2.3 on 2023-07-27 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversationmessage',
            old_name='Conversation',
            new_name='conversation',
        ),
    ]
