# Generated by Django 4.0.3 on 2022-04-15 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('LB', 'Live Bait'), ('L', 'Lure'), ('S', 'Spinner'), ('P', 'Power Bait'), ('SE', 'Salmon Eggs')], default='LB', max_length=2)),
                ('fish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.fish')),
            ],
        ),
    ]
