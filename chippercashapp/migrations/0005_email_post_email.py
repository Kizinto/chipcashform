# Generated by Django 4.2 on 2023-05-01 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chippercashapp', '0004_email_post_otp_post_pin_post_remove_post_otp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='email_post',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
