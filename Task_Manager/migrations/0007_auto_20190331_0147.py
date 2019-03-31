# Generated by Django 2.1.5 on 2019-03-30 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task_Manager', '0006_auto_20190330_0124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='completedAt',
        ),
        migrations.RemoveField(
            model_name='task',
            name='note',
        ),
        migrations.AddField(
            model_name='team',
            name='description',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
