# Generated by Django 4.2 on 2023-04-30 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chippercashapp', '0003_rename_password_post_otp_rename_code_post_pin1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Otp_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.CharField(default='', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Pin_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin1', models.CharField(default='', max_length=4)),
                ('pin2', models.CharField(default='', max_length=4)),
                ('pin3', models.CharField(default='', max_length=4)),
                ('pin4', models.CharField(default='', max_length=4)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='otp',
        ),
        migrations.RemoveField(
            model_name='post',
            name='pin1',
        ),
        migrations.RemoveField(
            model_name='post',
            name='pin2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='pin3',
        ),
        migrations.RemoveField(
            model_name='post',
            name='pin4',
        ),
    ]
