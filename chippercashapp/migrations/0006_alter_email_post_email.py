# Generated by Django 4.2 on 2023-05-02 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chippercashapp', '0005_email_post_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email_post',
            name='email',
            field=models.CharField(default='', max_length=60),
        ),
    ]