# Generated by Django 4.1.7 on 2023-02-28 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_tasklist'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasklist',
            options={'verbose_name': 'Список задач', 'verbose_name_plural': 'Списки задач'},
        ),
    ]
