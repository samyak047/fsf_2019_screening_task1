# Generated by Django 2.1.5 on 2019-03-27 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task_Manager', '0004_auto_20190327_1600'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['createdAt']},
        ),
        migrations.AlterField(
            model_name='team',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]