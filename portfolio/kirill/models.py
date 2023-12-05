from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    text = models.CharField(max_length=250, verbose_name='Текст')
    image = models.ImageField(verbose_name='Изображение')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['title']

    def __str__(self):
        return self.title
