# Generated by Django 5.0.2 on 2024-03-25 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('1', 'Наличные'), ('2', 'Перевод')], max_length=10, verbose_name='способ_оплаты'),
        ),
    ]
