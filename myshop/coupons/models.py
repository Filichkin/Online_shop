from django.core.validators import (
    MinValueValidator,
    MaxValueValidator
)
from django.db import models


class Coupon(models.Model):
    code = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Код купона'
    )
    valid_from = models.DateTimeField(
        verbose_name='Начало действия'
    )
    valid_to = models.DateTimeField(
        verbose_name='Окончание действия'
    )
    discount = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
            ],
        help_text='Уровень в процентах от 0 до 100',
        verbose_name='Скидка'
    )
    active = models.BooleanField(
        verbose_name='Статус активации'
    )

    def __str__(self):
        return self.code
