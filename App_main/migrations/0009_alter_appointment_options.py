# Generated by Django 4.2.1 on 2023-07-04 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_main', '0008_alter_appointment_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'ordering': ['-date', '-time']},
        ),
    ]
