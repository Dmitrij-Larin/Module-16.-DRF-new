# Generated by Django 5.2.1 on 2025-06-04 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0004_rename_questions_question'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['id'], 'verbose_name': 'Content', 'verbose_name_plural': 'Contents'},
        ),
    ]
