# Generated by Django 4.2.8 on 2024-01-27 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stocks', '0016_remove_userprofile_bio_remove_userprofile_birth_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='otp',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
