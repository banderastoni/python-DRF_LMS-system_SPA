from django.contrib.auth.models import AbstractUser
from django.db import models

from learning.models import Course, Lesson

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=12, **NULLABLE, verbose_name='телефон')
    city = models.CharField(max_length=100, **NULLABLE, verbose_name='город')
    avatar = models.ImageField(upload_to="users/", **NULLABLE, verbose_name='аватарка')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('pk',)


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='оплативший пользователь')
    payment_date = models.DateField(auto_now_add=True, verbose_name='дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='оплаченный курс', **NULLABLE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='оплаченный урок', **NULLABLE)
    payment_sum = models.PositiveIntegerField(verbose_name='сумма оплаты')
    payment_method = models.CharField(choices=[('1', 'Наличные'), ('2', 'Перевод')], verbose_name='способ оплаты')

    def __str__(self):
        return f"{self.user}: {self.course if self.course else self.lesson} - {self.payment_date}"

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
        ordering = ('-payment_date',)
