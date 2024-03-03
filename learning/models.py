from django.conf import settings
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='название_курса')
    description = models.TextField(verbose_name='описание_курса', **NULLABLE)
    image = models.ImageField(upload_to='courses/', verbose_name='превью_курса', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='название_урока')
    description = models.TextField(verbose_name='описание_урока')
    image = models.ImageField(upload_to='courses/lessons/', verbose_name='превью_урока', **NULLABLE)
    link = models.URLField(verbose_name='ссылка_на_видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='название_курса')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f"{self.course} - {self.title}"

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
