# Generated by Django 3.2.13 on 2022-06-12 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220610_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='link',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='time_minutes',
            field=models.IntegerField(),
        ),
    ]