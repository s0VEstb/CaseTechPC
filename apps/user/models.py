from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.conf import settings


class CustomUser(AbstractUser):
    """
    Расширенная модель пользователя.
    Уже содержит username, email, password, date_joined и т.п.
    """
    avatar          = models.ImageField(upload_to='avatars/', blank=True, null=True)
    # многие-ко-многим связь через Enrollment
    enrolled_topics = models.ManyToManyField(
        'course.Topic',
        through='course.Enrollment',
        related_name='students',
        blank=True,
        verbose_name='Записан на темы'
    )

    def __str__(self):
        return self.username
    
    