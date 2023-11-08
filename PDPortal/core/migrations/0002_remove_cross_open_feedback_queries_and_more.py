# Generated by Django 4.2.4 on 2023-11-08 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cross_open',
            name='feedback_queries',
        ),
        migrations.RemoveField(
            model_name='independent_adjudicator',
            name='feedback_queries',
        ),
        migrations.RemoveField(
            model_name='institutionalteam_contingent',
            name='alt_poc_number',
        ),
        migrations.RemoveField(
            model_name='institutionalteam_contingent',
            name='feedback_queries',
        ),
        migrations.AlterField(
            model_name='cross_open',
            name='email_id_head',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
    ]
