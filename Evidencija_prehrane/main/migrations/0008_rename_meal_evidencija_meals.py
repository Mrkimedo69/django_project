# Generated by Django 4.1.4 on 2022-12-16 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_evidencija_meal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evidencija',
            old_name='meal',
            new_name='meals',
        ),
    ]
