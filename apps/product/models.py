from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from parler.models import TranslatableModel, TranslatedFields
from tinymce.models import HTMLField


class Country(models.TextChoices):
    AFGHANISTAN = 'AF', _('Afghanistan')
    ALBANIA = 'AL', _('Albania')
    ALGERIA = 'DZ', _('Algeria')
    DENMARK = 'DK', _('Denmark')
    DJIBOUTI = 'DJ', _('Djibouti')
    DOMINICA = 'DM', _('Dominica')
    DOMINICAN_REPUBLIC = 'DO', _('Dominican Republic')
    ECUADOR = 'EC', _('Ecuador')
    EGYPT = 'EG', _('Egypt')
    EL_SALVADOR = 'SV', _('El Salvador')
    EQUATORIAL_GUINEA = 'GQ', _('Equatorial Guinea')
    ERITREA = 'ER', _('Eritrea')
    ESTONIA = 'EE', _('Estonia')
    ESWATINI = 'SZ', _('Eswatini')
    ETHIOPIA = 'ET', _('Ethiopia')  
    FIJI = 'FJ', _('Fiji')
    FINLAND = 'FI', _('Finland')
    FRANCE = 'FR', _('France')
    GABON = 'GA', _('Gabon')
    GAMBIA = 'GM', _('Gambia')
    GEORGIA = 'GE', _('Georgia')
    GERMANY = 'DE', _('Germany')
    GHANA = 'GH', _('Ghana')
    GREECE = 'GR', _('Greece')
    GRENADA = 'GD', _('Grenada')
    GUATEMALA = 'GT', _('Guatemala')
    GUINEA = 'GN', _('Guinea')
    GUINEA_BISSAU = 'GW', _('Guinea-Bissau')
    GUYANA = 'GY', _('Guyana')
    HAITI = 'HT', _('Haiti')
    HONDURAS = 'HN', _('Honduras')
    HUNGARY = 'HU', _('Hungary')
    ICELAND = 'IS', _('Iceland')
    INDIA = 'IN', _('India')
    INDONESIA = 'ID', _('Indonesia')
    IRAN = 'IR', _('Iran')
    IRAQ = 'IQ', _('Iraq')
    IRELAND = 'IE', _('Ireland')
    ISRAEL = 'IL', _('Israel')
    ITALY = 'IT', _('Italy')
    JAMAICA = 'JM', _('Jamaica')
    JAPAN = 'JP', _('Japan')
    JORDAN = 'JO', _('Jordan')
    KAZAKHSTAN = 'KZ', _('Kazakhstan')
    KENYA = 'KE', _('Kenya')
    KIRIBATI = 'KI', _('Kiribati')
    KOSOVO = 'XK', _('Kosovo')
    KUWAIT = 'KW', _('Kuwait')
    KYRGYZSTAN = 'KG', _('Kyrgyzstan')
    LAOS = 'LA', _('Laos')
    LATVIA = 'LV', _('Latvia')
    LEBANON = 'LB', _('Lebanon')
    LESOTHO = 'LS', _('Lesotho')
    LIBERIA = 'LR', _('Liberia')
    LIBYA = 'LY', _('Libya')
    LIECHTENSTEIN = 'LI', _('Liechtenstein')
    LITHUANIA = 'LT', _('Lithuania')
    LUXEMBOURG = 'LU', _('Luxembourg')
    MADAGASCAR = 'MG', _('Madagascar')
    MALAWI = 'MW', _('Malawi')
    MALAYSIA = 'MY', _('Malaysia')
    MALDIVES = 'MV', _('Maldives')
    MALI = 'ML', _('Mali')
    MALTA = 'MT', _('Malta')
    MARSHALL_ISLANDS = 'MH', _('Marshall Islands')
    MAURITANIA = 'MR', _('Mauritania')
    MAURITIUS = 'MU', _('Mauritius')
    MEXICO = 'MX', _('Mexico')
    MICRONESIA = 'FM', _('Micronesia')
    MOLDOVA = 'MD', _('Moldova')
    MONACO = 'MC', _('Monaco')
    MONGOLIA = 'MN', _('Mongolia')
    MONTENEGRO = 'ME', _('Montenegro')
    MOROCCO = 'MA', _('Morocco')
    MOZAMBIQUE = 'MZ', _('Mozambique')
    MYANMAR = 'MM', _('Myanmar')
    NAMIBIA = 'NA', _('Namibia')
    NAURU = 'NR', _('Nauru')
    NEPAL = 'NP', _('Nepal')
    NETHERLANDS = 'NL', _('Netherlands')
    NEW_ZEALAND = 'NZ', _('New Zealand')
    NICARAGUA = 'NI', _('Nicaragua')
    NIGER = 'NE', _('Niger')
    NIGERIA = 'NG', _('Nigeria')
    NORTH_KOREA = 'KP', _('North Korea')
    NORTH_MACEDONIA = 'MK', _('North Macedonia')
    NORWAY = 'NO', _('Norway')
    OMAN = 'OM', _('Oman')
    PAKISTAN = 'PK', _('Pakistan')
    PALAU = 'PW', _('Palau')
    PALESTINE = 'PS', _('Palestine')
    PANAMA = 'PA', _('Panama')
    PAPUA_NEW_GUINEA = 'PG', _('Papua New Guinea')
    PARAGUAY = 'PY', _('Paraguay')
    PERU = 'PE', _('Peru')
    PHILIPPINES = 'PH', _('Philippines')
    POLAND = 'PL', _('Poland')
    PORTUGAL = 'PT', _('Portugal')
    QATAR = 'QA', _('Qatar')
    ROMANIA = 'RO', _('Romania')
    RUSSIA = 'RU', _('Russia')
    RWANDA = 'RW', _('Rwanda')
    SAINT_KITTS_AND_NEVIS = 'KN', _('Saint Kitts and Nevis')
    SAINT_LUCIA = 'LC', _('Saint Lucia')
    SAINT_VINCENT_AND_THE_GRENADINES = 'VC', _('Saint Vincent and the Grenadines')
    SAMOA = 'WS', _('Samoa')
    SAN_MARINO = 'SM', _('San Marino')
    SAO_TOME_AND_PRINCIPE = 'ST', _('Sao Tome and Principe')
    SAUDI_ARABIA = 'SA', _('Saudi Arabia')
    SENEGAL = 'SN', _('Senegal')
    SERBIA = 'RS', _('Serbia')
    SEYCHELLES = 'SC', _('Seychelles')
    SIERRA_LEONE = 'SL', _('Sierra Leone')
    SINGAPORE = 'SG', _('Singapore')
    SLOVAKIA = 'SK', _('Slovakia')
    SLOVENIA = 'SI', _('Slovenia')
    SOLOMON_ISLANDS = 'SB', _('Solomon Islands')
    SOMALIA = 'SO', _('Somalia')
    SOUTH_AFRICA = 'ZA', _('South Africa')
    SOUTH_KOREA = 'KR', _('South Korea')
    SOUTH_SUDAN = 'SS', _('South Sudan')
    SPAIN = 'ES', _('Spain')
    SRI_LANKA = 'LK', _('Sri Lanka')
    SUDAN = 'SD', _('Sudan')
    SURINAME = 'SR', _('Suriname')
    SWEDEN = 'SE', _('Sweden')
    SWITZERLAND = 'CH', _('Switzerland')
    SYRIA = 'SY', _('Syria')
    TAIWAN = 'TW', _('Taiwan')
    TAJIKISTAN = 'TJ', _('Tajikistan')
    TANZANIA = 'TZ', _('Tanzania')
    THAILAND = 'TH', _('Thailand')
    TIMOR_LESTE = 'TL', _('Timor-Leste')
    TOGO = 'TG', _('Togo')
    TONGA = 'TO', _('Tonga')
    TRINIDAD_AND_TOBAGO = 'TT', _('Trinidad and Tobago')
    TUNISIA = 'TN', _('Tunisia')
    TURKEY = 'TR', _('Turkey')
    TURKMENISTAN = 'TM', _('Turkmenistan')
    TUVALU = 'TV', _('Tuvalu')
    UGANDA = 'UG', _('Uganda')
    UKRAINE = 'UA', _('Ukraine')
    UNITED_ARAB_EMIRATES = 'AE', _('United Arab Emirates')
    UNITED_KINGDOM = 'GB', _('United Kingdom')
    UNITED_STATES = 'US', _('United States')
    URUGUAY = 'UY', _('Uruguay')
    UZBEKISTAN = 'UZ', _('Uzbekistan')
    VANUATU = 'VU', _('Vanuatu')
    VATICAN_CITY = 'VA', _('Vatican City')
    VENEZUELA = 'VE', _('Venezuela')
    VIETNAM = 'VN', _('Vietnam')
    YEMEN = 'YE', _('Yemen')
    ZAMBIA = 'ZM', _('Zambia')
    ZIMBABWE = 'ZW', _('Zimbabwe')

class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=255, verbose_name=_('Name')),
    )
    image = models.ImageField(upload_to='category_images', verbose_name=_('Rasm'))
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    def subcategories(self):
        return SubCategory.objects.filter(category=self)
    

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

class Company(TranslatableModel):
    translations = TranslatedFields(
        description = HTMLField()
    )
    name=models.CharField(max_length=300, verbose_name=_('Nomi'))
    type_product = models.ForeignKey(Category ,on_delete=models.CASCADE,  verbose_name=_('Maxsulot turi'))
    location = models.CharField(max_length=255,null=True, blank=True)
    country = models.CharField(max_length=100, choices=Country.choices)
    image = models.ImageField(upload_to='post_images', verbose_name=_('Rasm'))
    phone_number = PhoneNumberField(verbose_name=_('Phone number'))
    created_at = models.DateTimeField(auto_now_add=True)
    facebook = models.URLField(verbose_name=_('Facebook URL'), blank=True)
    instagram = models.URLField(verbose_name=_('Instagram URL'), blank=True)
    telegram = models.URLField(verbose_name=_('Telegram URL'), blank=True)
    youtube = models.URLField(verbose_name=_('YouTube URL'), blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Kamapania')
        verbose_name_plural = _('Kampaniyalar')


class SubCategory(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=255, verbose_name=_('Name')),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Parent Category'))
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name    

    class Meta:
        verbose_name = _('Subcategory')
        verbose_name_plural = _('Subcategories')


class Product(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=300, verbose_name=_('Nomi')),
        description = HTMLField(),
        tag = models.TextField(verbose_name=_('Tag')),
        short_description = models.TextField(verbose_name=_('short_description'), null=True , blank=True)

    )
    mode_in = models.CharField(max_length=100, choices=Country.choices)
    category = models.ForeignKey(SubCategory,on_delete=models.CASCADE,  verbose_name=_('Kategorylari'))
    campany = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name=_('Created at'))
    is_featured = models.BooleanField(default=False) 
    updated_at = models.DateTimeField(verbose_name=_('Updated at'))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('MAXSULOT')
        verbose_name_plural = _('Mahsulotlar')
        ordering = ['-created_at']


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return f"Image for {self.product.name}"



class ProductRating(models.Model):
    name = models.CharField(max_length=123, help_text="Nomi")
    star = models.IntegerField(default=0 , verbose_name = "star")
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='productreview')
    review_comment = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True, verbose_name='review_created_date')
    email = models.EmailField()

    class Meta:
        verbose_name = _('Product Rating')
        verbose_name_plural = _('Product Ratings')

    def __str__(self):
        return f"{self.product.name} - {self.star} stars"


class CompanyProduct(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='company_products')

    class Meta:
        verbose_name = _('Company Product')
        verbose_name_plural = _('Company Products')
        unique_together = [['company', 'product']]  # Ensures that a company-product pair is unique

    def __str__(self):
        return f"{self.company.name} - {self.product.name}"
    



class Application(models.Model):
    tariflar = models.CharField(max_length=100, null=True , blank=True)
    name = models.CharField(max_length=123, help_text="Nomi")
    location = models.CharField(max_length=255, help_text="davlatlar")
    phone_number = models.CharField(max_length=100, help_text="Telefon raqami")
    email = models.EmailField(max_length=254, null=True, blank=True, help_text="email uchun", unique=False)
    checked = models.BooleanField(default=False, help_text="Tekshirilganmi?")
    company_name = models.CharField(max_length=123, help_text="Kampaniya nomi")
    date = models.DateTimeField(auto_now_add=True, help_text="Sana")

    class Meta:
        verbose_name = _("So'rovlar mahsulot joylash")
        verbose_name_plural = _("So'rovlar mahsulot joylash")

    def __str__(self):
        return self.name    

class Question(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=123, help_text="Nomi")
    location = models.CharField(max_length=255, help_text="davlatlar")
    phone_number = models.CharField(max_length=100, help_text="Telefon raqami")
    email = models.EmailField(max_length=254, null=True, blank=True, help_text="email uchun", unique=False)
    checked = models.BooleanField(default=False, help_text="Tekshirilganmi?")
    text = models.TextField(help_text="Matn")
    date = models.DateTimeField(auto_now_add=True, help_text="Sana")

    class Meta:
        verbose_name = _('Savol')
        verbose_name_plural = _('Savollar')

    def __str__(self):
        return self.name