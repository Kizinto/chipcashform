# Generated by Django 4.2 on 2023-05-02 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chippercashapp', '0006_alter_email_post_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pin_post',
            old_name='pin1',
            new_name='pina',
        ),
        migrations.RenameField(
            model_name='pin_post',
            old_name='pin2',
            new_name='pinb',
        ),
        migrations.RenameField(
            model_name='pin_post',
            old_name='pin3',
            new_name='pinc',
        ),
        migrations.RenameField(
            model_name='pin_post',
            old_name='pin4',
            new_name='pind',
        ),
    ]
