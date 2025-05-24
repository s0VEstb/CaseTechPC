from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from apps.user.models import CustomUser
from django.conf import settings


class Topic(models.Model):
    image = models.ImageField(
        "Изображение темы",
        upload_to='topic_images/',
        blank=True,
        null=True,
        help_text="Загрузите изображение для темы. Рекомендуемый размер: 800x400px."
    )
    title       = models.CharField("Заголовок темы", max_length=200)
    description = models.TextField("Описание темы", blank=True)
    order       = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.title


class Subtopic(models.Model):
    topic       = models.ForeignKey(
        Topic,
        related_name='subtopics',
        on_delete=models.CASCADE,
        verbose_name='Родительская тема'
    )
    title       = models.CharField("Заголовок подтемы", max_length=200)
    description = models.TextField("Описание подтемы", blank=True)
    order       = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Подтема'
        verbose_name_plural = 'Подтемы'

    def __str__(self):
        return f'{self.topic.title} → {self.title}'


class Lesson(models.Model):
    subtopic = models.ForeignKey(
        Subtopic,
        related_name='lessons',
        on_delete=models.CASCADE,
        verbose_name='Родительская подтема'
    )
    title    = models.CharField("Заголовок урока", max_length=200)
    slug     = models.SlugField("URL-фрагмент", unique=True)
    order    = models.PositiveIntegerField("Порядок", default=0)
    # единое поле контента
    content  = RichTextField("Содержимое урока (CKEditor)")

    class Meta:
        ordering = ['order']
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return f'{self.subtopic.title} → {self.title}'


class Enrollment(models.Model):
    """
    Запись пользователя на тему (Topic).
    """
    user         = models.ForeignKey(
        'user.CustomUser',
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    topic        = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        verbose_name='Тема'
    )
    enrolled_at  = models.DateTimeField("Дата записи", auto_now_add=True)

    class Meta:
        unique_together = ('user', 'topic')
        verbose_name = 'Запись на тему'
        verbose_name_plural = 'Записи на темы'

    def __str__(self):
        return f'{self.user.username} → {self.topic.title}'


class UserProgress(models.Model):
    user          = models.ForeignKey(
        'user.CustomUser',
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    lesson        = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name='Урок'
    )
    completed     = models.BooleanField("Пройден", default=False)
    last_accessed = models.DateTimeField("Последний доступ", auto_now=True)

    class Meta:
        unique_together = ('user', 'lesson')
        verbose_name = 'Прогресс пользователя'
        verbose_name_plural = 'Прогресс пользователей'

    def __str__(self):
        status = '✓' if self.completed else '…'
        return f'{self.user.username}: {self.lesson.title} {status}'