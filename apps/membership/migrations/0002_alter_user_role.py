# Generated by Django 3.2.12 on 2022-11-18 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveIntegerField(choices=[(1, 'User'), (2, 'Editor'), (3, 'Super Admin')], default=1, verbose_name='User role'),
        ),
    ]
