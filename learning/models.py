from django.db import models
from users.models import NULLABLE


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='название курса')
    description = models.TextField(verbose_name='описание курса', **NULLABLE)
    image = models.ImageField(upload_to='courses/', verbose_name='превью курса', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='название урока')
    description = models.TextField(verbose_name='описание урока')
    image = models.ImageField(upload_to='courses/lessons/', verbose_name='превью урока', **NULLABLE)
    link = models.URLField(verbose_name='ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='название курса')

    def __str__(self):
        return f"{self.course} - {self.title}"

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
