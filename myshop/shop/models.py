from django.db import models


CATEGORY_MAX_LENGTH = 256
PRODUCT_MAX_LENGTH = 200


class Category(models.Model):
    name = models.CharField(
        max_length=CATEGORY_MAX_LENGTH,
        verbose_name='Название категории'
        )
    slug = models.SlugField(
        max_length=CATEGORY_MAX_LENGTH,
        unique=True,
        verbose_name='Идентификатор'
        )

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        related_name='products',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=PRODUCT_MAX_LENGTH,
        verbose_name='Название товара'
        )
    slug = models.SlugField(
        max_length=PRODUCT_MAX_LENGTH,
        verbose_name='Идентификатор'
        )
    image = models.ImageField(
        upload_to='products/%Y/%m/%d',
        blank=True,
        verbose_name='Фото товара'
    )
    description = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена'
        )
    available = models.BooleanField(
        default=True,
        verbose_name='Наличие'
        )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время размещения'
        )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата и время обновления')

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
