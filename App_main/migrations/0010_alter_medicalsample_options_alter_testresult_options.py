# Generated by Django 4.2.1 on 2023-07-04 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_main', '0009_alter_appointment_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicalsample',
            options={'ordering': ['-collection_date', '-collection_time']},
        ),
        migrations.AlterModelOptions(
            name='testresult',
            options={'ordering': ['-date_processed']},
        ),
    ]
