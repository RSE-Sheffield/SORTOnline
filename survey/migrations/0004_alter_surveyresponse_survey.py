# Generated by Django 5.1.2 on 2025-01-15 19:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_alter_survey_description_alter_survey_survey_config'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyresponse',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_response', to='survey.survey'),
        ),
    ]
