# Generated by Django 2.2.7 on 2024-03-13 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('haircuts', '0003_haircut_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='haircut',
            name='person',
        ),
    ]
