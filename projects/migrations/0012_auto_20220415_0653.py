# Generated by Django 2.2.27 on 2022-04-15 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20220414_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk',
            name='impact',
            field=models.CharField(choices=[('VL', 'Very Low'), ('L', 'Low'), ('M', 'Medium'), ('H', 'High'), ('VH', 'Very High')], max_length=2),
        ),
        migrations.AlterField(
            model_name='risk',
            name='probability',
            field=models.CharField(choices=[('VL', 'Very Low'), ('L', 'Low'), ('M', 'Medium'), ('H', 'High'), ('VH', 'Very High')], max_length=2),
        ),
    ]
