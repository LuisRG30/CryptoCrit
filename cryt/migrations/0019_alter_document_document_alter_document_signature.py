# Generated by Django 4.0.3 on 2022-04-23 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryt', '0018_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(null=True, upload_to='documents'),
        ),
        migrations.AlterField(
            model_name='document',
            name='signature',
            field=models.FileField(null=True, upload_to='signatures'),
        ),
    ]