# Generated by Django 2.2.27 on 2022-04-02 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_auto_20220402_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.IntegerField(choices=[(4, 'Urgent'), (3, 'High'), (2, 'Medium'), (1, 'Low')], default=1),
        ),
    ]
