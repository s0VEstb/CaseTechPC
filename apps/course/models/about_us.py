from django.db import models
from django.conf import settings


class AboutUs(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField("Изображение", upload_to='about_us/', blank=True, null=True)

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.title
    

class TeamMember(models.Model):
    name = models.CharField("Имя", max_length=200)
    position = models.CharField("Должность", max_length=200)
    bio = models.TextField("Биография", blank=True)
    image = models.ImageField("Изображение", upload_to='team_members/', blank=True, null=True)
    

    class Meta:
        verbose_name = 'Член команды'
        verbose_name_plural = 'Члены команды'

    def __str__(self):
        return self.name
    

