# Generated by Django 4.2.11 on 2024-03-18 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0003_alter_companytranslation_short_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Telefon Raqami')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan Vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Yangilangan Vaqti')),
                ('is_processed', models.BooleanField(default=False, verbose_name='Qayta ishlandimi?')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Foydalanuvchi')),
            ],
            options={
                'verbose_name': 'Buyurtma',
                'verbose_name_plural': 'Buyurtmalar',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Miqdori')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='product.order', verbose_name='Buyurtma')),
            ],
            options={
                'verbose_name': 'Buyurtma Bandidagi Mahsulot',
                'verbose_name_plural': 'Buyurtma Bandidagi Mahsulotlar',
            },
        ),
        migrations.DeleteModel(
            name='Application',
        ),
        migrations.AlterUniqueTogether(
            name='companytranslation',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='companytranslation',
            name='master',
        ),
        migrations.AlterUniqueTogether(
            name='positiontranslation',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='positiontranslation',
            name='master',
        ),
        migrations.RemoveField(
            model_name='productrating',
            name='product',
        ),
        migrations.RemoveField(
            model_name='question',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='company',
        ),
        migrations.RemoveField(
            model_name='product',
            name='mode_in',
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='CompanyTranslation',
        ),
        migrations.DeleteModel(
            name='Position',
        ),
        migrations.DeleteModel(
            name='PositionTranslation',
        ),
        migrations.DeleteModel(
            name='ProductRating',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Mahsulot'),
        ),
    ]