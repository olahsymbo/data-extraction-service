# Generated by Django 3.2 on 2022-09-21 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskdata',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
