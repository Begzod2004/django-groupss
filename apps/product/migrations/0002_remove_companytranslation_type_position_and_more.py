# Generated by Django 4.1.7 on 2023-09-25 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '__first__'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companytranslation',
            name='type_position',
        ),
        migrations.AddField(
            model_name='company',
            name='type_position',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.position', verbose_name='Biznes turi turi'),
            preserve_default=False,
        ),
    ]
