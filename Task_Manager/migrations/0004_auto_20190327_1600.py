# Generated by Django 2.1.5 on 2019-03-27 10:30

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Task_Manager', '0003_auto_20190326_2157'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['createdAt']},
        ),
        migrations.AddField(
            model_name='task',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Task_Manager.Team'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='team',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
