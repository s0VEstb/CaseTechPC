from django.db import models
from django.core.validators import RegexValidator


kyrgyz_phone_regex = RegexValidator(
    regex=r'^\+996\d{9}$',
    message="Номер должен быть в формате: '+996XXXXXXXXX' (всего 13 символов)."
)

class Contacts(models.Model):
    number =  models.CharField(
        validators=[kyrgyz_phone_regex],
        max_length=13,
        unique=True,
        help_text="Введите номер в формате: +996XXXXXXXXX"
    )
    email = models.EmailField(("Электронная почта"), max_length=254)
    link_1 = models.URLField(("Ссылка VK"), max_length=200, blank=True, null=True)
    link_2 = models.URLField(("Ссылка Telegram"), max_length=200, blank=True, null=True)
    link_3 = models.URLField(("Ссылка WhatsApp"), max_length=200, blank=True, null=True)
    link_4 = models.URLField(("Ссылка Instagram"), max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Контакты: {self.number}, {self.email}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"