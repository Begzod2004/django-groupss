# Generated by Django 4.1.7 on 2023-09-09 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_alter_companytranslation_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producttranslation',
            name='compound',
        ),
    ]
