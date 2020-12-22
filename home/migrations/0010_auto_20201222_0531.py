# Generated by Django 3.1.3 on 2020-12-22 05:31
# This migration creates groups
from django.db import migrations


class Migration(migrations.Migration):

    def add_groups(apps, schema_editor):
        Group = apps.get_model('auth', 'Group')
        Group.objects.bulk_create([
            Group(name='end_users'),
            Group(name='developers'),
            Group(name='project_managers')
        ])

    dependencies = [
        ('home', '0009_auto_20201220_1011'),
    ]

    operations = [
        migrations.RunPython(add_groups)
    ]