# Generated by Django 4.0.3 on 2022-04-20 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryt', '0011_alter_userprofile_p12'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='p12',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='pem',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]