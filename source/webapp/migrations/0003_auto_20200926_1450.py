# Generated by Django 2.2 on 2020-09-26 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20200926_1215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='review',
            new_name='text_review',
        ),
    ]
