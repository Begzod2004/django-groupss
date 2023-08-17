# Generated by Django 4.1.7 on 2023-08-17 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_application_question'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'verbose_name': "So'rovlar mahsulot joylash", 'verbose_name_plural': "So'rovlar mahsulot joylash"},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Savol', 'verbose_name_plural': 'Savollar'},
        ),
        migrations.AddField(
            model_name='productrating',
            name='name',
            field=models.CharField(default=1, help_text='Nomi', max_length=123),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producttranslation',
            name='description',
            field=models.CharField(default=1, max_length=1000, verbose_name='maxsulot haqida qisqacha'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='phone_number',
            field=models.CharField(help_text='Telefon raqami', max_length=100),
        ),
    ]
