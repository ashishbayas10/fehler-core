# Generated by Django 2.2.27 on 2022-04-16 16:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spaces', '0005_auto_20220416_1621'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='spacemembership',
            unique_together={('space', 'member')},
        ),
    ]
