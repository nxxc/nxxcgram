# Generated by Django 2.0.9 on 2018-10-12 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_auto_20181012_1500'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-created_at']},
        ),
    ]