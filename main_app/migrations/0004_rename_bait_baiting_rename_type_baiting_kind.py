# Generated by Django 4.0.3 on 2022-04-16 00:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_bait_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bait',
            new_name='Baiting',
        ),
        migrations.RenameField(
            model_name='baiting',
            old_name='type',
            new_name='kind',
        ),
    ]
