# Generated by Django 5.2 on 2025-05-06 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='lead',
            name='phone',
            field=models.CharField(default='0000000000', max_length=15),
        ),
        migrations.AddField(
            model_name='lead',
            name='segment',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
