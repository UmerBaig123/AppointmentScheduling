# Generated by Django 4.2.13 on 2024-06-24 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_userdata_citizenship_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isAvailable', models.BooleanField()),
                ('url', models.CharField(max_length=100)),
            ],
        ),
    ]
