from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from parler.models import TranslatableModel, TranslatedFields
from tinymce.models import HTMLField


class Position(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=255, verbose_name=_('Name')),
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Nima bilan shug'ullanadi")
        verbose_name_plural = _('Pazitsiyalar')