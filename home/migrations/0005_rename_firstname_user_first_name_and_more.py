# Generated by Django 5.1.2 on 2025-01-10 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_project_alter_organisation_projects'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='lastname',
            new_name='last_name',
        ),
    ]