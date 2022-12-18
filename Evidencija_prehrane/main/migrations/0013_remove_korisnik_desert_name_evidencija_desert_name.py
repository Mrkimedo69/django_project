# Generated by Django 4.0.5 on 2022-12-17 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_korisnik_desert_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='korisnik',
            name='desert_name',
        ),
        migrations.AddField(
            model_name='evidencija',
            name='desert_name',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.desert'),
        ),
    ]
