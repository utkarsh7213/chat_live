# Generated by Django 4.0.3 on 2022-05-02 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpAddr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_addr', models.CharField(max_length=15)),
            ],
        ),
    ]
