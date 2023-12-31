# Generated by Django 4.1.7 on 2023-09-29 22:53

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models
import phonenumber_field.modelfields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarif', models.CharField(blank=True, default='Рынок Узбекистана', max_length=100, null=True, verbose_name='Tarif')),
                ('name', models.CharField(help_text='Nomi', max_length=123, verbose_name='Name')),
                ('location', models.CharField(help_text='Davlatlar', max_length=255, verbose_name='Location')),
                ('phone_number', models.CharField(help_text='Telefon raqami', max_length=100, verbose_name='Phone Number')),
                ('email', models.EmailField(blank=True, help_text='Email uchun', max_length=254, null=True, verbose_name='Email')),
                ('checked', models.BooleanField(default=False, help_text='Tekshirilganmi?', verbose_name='Checked')),
                ('company_name', models.CharField(help_text='Kampaniya nomi', max_length=123, verbose_name='Company Name')),
                ('date', models.DateTimeField(auto_now_add=True, help_text='Sana', verbose_name='Date')),
            ],
            options={
                'verbose_name': 'Application',
                'verbose_name_plural': 'Applications',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='category_images', verbose_name='Rasm')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Nomi')),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(choices=[('AF', 'Afghanistan'), ('AL', 'Albania'), ('DZ', 'Algeria'), ('DK', 'Denmark'), ('DJ', 'Djibouti'), ('DM', 'Dominica'), ('DO', 'Dominican Republic'), ('EC', 'Ecuador'), ('EG', 'Egypt'), ('SV', 'El Salvador'), ('GQ', 'Equatorial Guinea'), ('ER', 'Eritrea'), ('EE', 'Estonia'), ('SZ', 'Eswatini'), ('ET', 'Ethiopia'), ('FJ', 'Fiji'), ('FI', 'Finland'), ('FR', 'France'), ('GA', 'Gabon'), ('GM', 'Gambia'), ('GE', 'Georgia'), ('DE', 'Germany'), ('GH', 'Ghana'), ('GR', 'Greece'), ('GD', 'Grenada'), ('GT', 'Guatemala'), ('GN', 'Guinea'), ('GW', 'Guinea-Bissau'), ('GY', 'Guyana'), ('HT', 'Haiti'), ('HN', 'Honduras'), ('HU', 'Hungary'), ('IS', 'Iceland'), ('IN', 'India'), ('ID', 'Indonesia'), ('IR', 'Iran'), ('IQ', 'Iraq'), ('IE', 'Ireland'), ('IL', 'Israel'), ('IT', 'Italy'), ('JM', 'Jamaica'), ('JP', 'Japan'), ('JO', 'Jordan'), ('KZ', 'Kazakhstan'), ('KE', 'Kenya'), ('KI', 'Kiribati'), ('XK', 'Kosovo'), ('KW', 'Kuwait'), ('KG', 'Kyrgyzstan'), ('LA', 'Laos'), ('LV', 'Latvia'), ('LB', 'Lebanon'), ('LS', 'Lesotho'), ('LR', 'Liberia'), ('LY', 'Libya'), ('LI', 'Liechtenstein'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('MG', 'Madagascar'), ('MW', 'Malawi'), ('MY', 'Malaysia'), ('MV', 'Maldives'), ('ML', 'Mali'), ('MT', 'Malta'), ('MH', 'Marshall Islands'), ('MR', 'Mauritania'), ('MU', 'Mauritius'), ('MX', 'Mexico'), ('FM', 'Micronesia'), ('MD', 'Moldova'), ('MC', 'Monaco'), ('MN', 'Mongolia'), ('ME', 'Montenegro'), ('MA', 'Morocco'), ('MZ', 'Mozambique'), ('MM', 'Myanmar'), ('NA', 'Namibia'), ('NR', 'Nauru'), ('NP', 'Nepal'), ('NL', 'Netherlands'), ('NZ', 'New Zealand'), ('NI', 'Nicaragua'), ('NE', 'Niger'), ('NG', 'Nigeria'), ('KP', 'North Korea'), ('MK', 'North Macedonia'), ('NO', 'Norway'), ('OM', 'Oman'), ('PK', 'Pakistan'), ('PW', 'Palau'), ('PS', 'Palestine'), ('PA', 'Panama'), ('PG', 'Papua New Guinea'), ('PY', 'Paraguay'), ('PE', 'Peru'), ('PH', 'Philippines'), ('PL', 'Poland'), ('PT', 'Portugal'), ('QA', 'Qatar'), ('RO', 'Romania'), ('RU', 'Russia'), ('RW', 'Rwanda'), ('KN', 'Saint Kitts and Nevis'), ('LC', 'Saint Lucia'), ('VC', 'Saint Vincent and the Grenadines'), ('WS', 'Samoa'), ('SM', 'San Marino'), ('ST', 'Sao Tome and Principe'), ('SA', 'Saudi Arabia'), ('SN', 'Senegal'), ('RS', 'Serbia'), ('SC', 'Seychelles'), ('SL', 'Sierra Leone'), ('SG', 'Singapore'), ('SK', 'Slovakia'), ('SI', 'Slovenia'), ('SB', 'Solomon Islands'), ('SO', 'Somalia'), ('ZA', 'South Africa'), ('KR', 'South Korea'), ('SS', 'South Sudan'), ('ES', 'Spain'), ('LK', 'Sri Lanka'), ('SD', 'Sudan'), ('SR', 'Suriname'), ('SE', 'Sweden'), ('CH', 'Switzerland'), ('SY', 'Syria'), ('TW', 'Taiwan'), ('TJ', 'Tajikistan'), ('TZ', 'Tanzania'), ('TH', 'Thailand'), ('TL', 'Timor-Leste'), ('TG', 'Togo'), ('TO', 'Tonga'), ('TT', 'Trinidad and Tobago'), ('TN', 'Tunisia'), ('TR', 'Turkey'), ('TM', 'Turkmenistan'), ('TV', 'Tuvalu'), ('UG', 'Uganda'), ('UA', 'Ukraine'), ('AE', 'United Arab Emirates'), ('GB', 'United Kingdom'), ('US', 'United States'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VU', 'Vanuatu'), ('VA', 'Vatican City'), ('VE', 'Venezuela'), ('VN', 'Vietnam'), ('YE', 'Yemen'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe')], max_length=2)),
                ('image', models.ImageField(upload_to='post_images', verbose_name='Rasm')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone number')),
                ('workers_amount', models.CharField(help_text='masalan 5-10 va 10 - 15', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('found_year', models.CharField(help_text='masalan 2019 va 2023 yani found date', max_length=255)),
                ('facebook', models.URLField(blank=True, verbose_name='Facebook URL')),
                ('instagram', models.URLField(blank=True, verbose_name='Instagram URL')),
                ('telegram', models.URLField(blank=True, verbose_name='Telegram URL')),
                ('youtube', models.URLField(blank=True, verbose_name='YouTube URL')),
            ],
            options={
                'verbose_name': 'Kampania',
                'verbose_name_plural': 'Kampaniyalar',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': "Nima bilan shug'ullanadi",
                'verbose_name_plural': 'Pazitsiyalar',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode_in', models.CharField(choices=[('AF', 'Afghanistan'), ('AL', 'Albania'), ('DZ', 'Algeria'), ('DK', 'Denmark'), ('DJ', 'Djibouti'), ('DM', 'Dominica'), ('DO', 'Dominican Republic'), ('EC', 'Ecuador'), ('EG', 'Egypt'), ('SV', 'El Salvador'), ('GQ', 'Equatorial Guinea'), ('ER', 'Eritrea'), ('EE', 'Estonia'), ('SZ', 'Eswatini'), ('ET', 'Ethiopia'), ('FJ', 'Fiji'), ('FI', 'Finland'), ('FR', 'France'), ('GA', 'Gabon'), ('GM', 'Gambia'), ('GE', 'Georgia'), ('DE', 'Germany'), ('GH', 'Ghana'), ('GR', 'Greece'), ('GD', 'Grenada'), ('GT', 'Guatemala'), ('GN', 'Guinea'), ('GW', 'Guinea-Bissau'), ('GY', 'Guyana'), ('HT', 'Haiti'), ('HN', 'Honduras'), ('HU', 'Hungary'), ('IS', 'Iceland'), ('IN', 'India'), ('ID', 'Indonesia'), ('IR', 'Iran'), ('IQ', 'Iraq'), ('IE', 'Ireland'), ('IL', 'Israel'), ('IT', 'Italy'), ('JM', 'Jamaica'), ('JP', 'Japan'), ('JO', 'Jordan'), ('KZ', 'Kazakhstan'), ('KE', 'Kenya'), ('KI', 'Kiribati'), ('XK', 'Kosovo'), ('KW', 'Kuwait'), ('KG', 'Kyrgyzstan'), ('LA', 'Laos'), ('LV', 'Latvia'), ('LB', 'Lebanon'), ('LS', 'Lesotho'), ('LR', 'Liberia'), ('LY', 'Libya'), ('LI', 'Liechtenstein'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('MG', 'Madagascar'), ('MW', 'Malawi'), ('MY', 'Malaysia'), ('MV', 'Maldives'), ('ML', 'Mali'), ('MT', 'Malta'), ('MH', 'Marshall Islands'), ('MR', 'Mauritania'), ('MU', 'Mauritius'), ('MX', 'Mexico'), ('FM', 'Micronesia'), ('MD', 'Moldova'), ('MC', 'Monaco'), ('MN', 'Mongolia'), ('ME', 'Montenegro'), ('MA', 'Morocco'), ('MZ', 'Mozambique'), ('MM', 'Myanmar'), ('NA', 'Namibia'), ('NR', 'Nauru'), ('NP', 'Nepal'), ('NL', 'Netherlands'), ('NZ', 'New Zealand'), ('NI', 'Nicaragua'), ('NE', 'Niger'), ('NG', 'Nigeria'), ('KP', 'North Korea'), ('MK', 'North Macedonia'), ('NO', 'Norway'), ('OM', 'Oman'), ('PK', 'Pakistan'), ('PW', 'Palau'), ('PS', 'Palestine'), ('PA', 'Panama'), ('PG', 'Papua New Guinea'), ('PY', 'Paraguay'), ('PE', 'Peru'), ('PH', 'Philippines'), ('PL', 'Poland'), ('PT', 'Portugal'), ('QA', 'Qatar'), ('RO', 'Romania'), ('RU', 'Russia'), ('RW', 'Rwanda'), ('KN', 'Saint Kitts and Nevis'), ('LC', 'Saint Lucia'), ('VC', 'Saint Vincent and the Grenadines'), ('WS', 'Samoa'), ('SM', 'San Marino'), ('ST', 'Sao Tome and Principe'), ('SA', 'Saudi Arabia'), ('SN', 'Senegal'), ('RS', 'Serbia'), ('SC', 'Seychelles'), ('SL', 'Sierra Leone'), ('SG', 'Singapore'), ('SK', 'Slovakia'), ('SI', 'Slovenia'), ('SB', 'Solomon Islands'), ('SO', 'Somalia'), ('ZA', 'South Africa'), ('KR', 'South Korea'), ('SS', 'South Sudan'), ('ES', 'Spain'), ('LK', 'Sri Lanka'), ('SD', 'Sudan'), ('SR', 'Suriname'), ('SE', 'Sweden'), ('CH', 'Switzerland'), ('SY', 'Syria'), ('TW', 'Taiwan'), ('TJ', 'Tajikistan'), ('TZ', 'Tanzania'), ('TH', 'Thailand'), ('TL', 'Timor-Leste'), ('TG', 'Togo'), ('TO', 'Tonga'), ('TT', 'Trinidad and Tobago'), ('TN', 'Tunisia'), ('TR', 'Turkey'), ('TM', 'Turkmenistan'), ('TV', 'Tuvalu'), ('UG', 'Uganda'), ('UA', 'Ukraine'), ('AE', 'United Arab Emirates'), ('GB', 'United Kingdom'), ('US', 'United States'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VU', 'Vanuatu'), ('VA', 'Vatican City'), ('VE', 'Venezuela'), ('VN', 'Vietnam'), ('YE', 'Yemen'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe')], default='UZ', max_length=2)),
                ('created_at', models.DateTimeField(verbose_name='Created at')),
                ('is_featured', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(verbose_name='Updated at')),
            ],
            options={
                'verbose_name': 'MAXSULOT',
                'verbose_name_plural': 'Mahsulotlar',
                'ordering': ['-created_at'],
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Parent Category')),
            ],
            options={
                'verbose_name': 'Subcategory',
                'verbose_name_plural': 'Subcategories',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nomi', max_length=123, verbose_name='Name')),
                ('location', models.CharField(default='Uzbekistan', help_text='Davlatlar', max_length=255, verbose_name='Location')),
                ('phone_number', models.CharField(help_text='Telefon raqami', max_length=100, verbose_name='Phone Number')),
                ('email', models.EmailField(blank=True, help_text='Email uchun', max_length=254, null=True, verbose_name='Email')),
                ('checked', models.BooleanField(default=False, help_text='Tekshirilganmi?', verbose_name='Checked')),
                ('text', models.TextField(help_text='Matn', verbose_name='Text')),
                ('date', models.DateTimeField(auto_now_add=True, help_text='Sana', verbose_name='Date')),
                ('product_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='ProductRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nomi', max_length=123)),
                ('star', models.IntegerField(default=0, verbose_name='star')),
                ('review_comment', models.TextField()),
                ('review_date', models.DateTimeField(auto_now_add=True, verbose_name='review_created_date')),
                ('email', models.EmailField(max_length=254)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productreview', to='product.product')),
            ],
            options={
                'verbose_name': 'Product Rating',
                'verbose_name_plural': 'Product Ratings',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.subcategory', verbose_name='Kategorylari'),
        ),
        migrations.AddField(
            model_name='product',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.company'),
        ),
        migrations.AddField(
            model_name='company',
            name='type_position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.position', verbose_name='Biznes turi turi'),
        ),
        migrations.AddField(
            model_name='company',
            name='type_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Maxsulot turi'),
        ),
        migrations.CreateModel(
            name='SubCategoryTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='product.subcategory')),
            ],
            options={
                'verbose_name': 'Subcategory Translation',
                'db_table': 'product_subcategory_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ProductTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=300, verbose_name='Nomi')),
                ('description', tinymce.models.HTMLField()),
                ('tag', models.TextField(verbose_name='Tag')),
                ('short_description', models.TextField(blank=True, default='NEW', null=True, verbose_name='short_description')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='product.product')),
            ],
            options={
                'verbose_name': 'MAXSULOT Translation',
                'db_table': 'product_product_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PositionTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='product.position')),
            ],
            options={
                'verbose_name': "Nima bilan shug'ullanadi Translation",
                'db_table': 'product_position_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CompanyTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('short_description', models.TextField(blank=True, default='NEW', null=True, verbose_name='Short Description')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='product.company')),
            ],
            options={
                'verbose_name': 'Kampania Translation',
                'db_table': 'product_company_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='product.category')),
            ],
            options={
                'verbose_name': 'Category Translation',
                'db_table': 'product_category_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
