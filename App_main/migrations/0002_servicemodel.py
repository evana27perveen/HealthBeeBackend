# Generated by Django 4.1.4 on 2023-05-17 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=100)),
                ('price', models.FloatField(default=0)),
            ],
        ),
    ]