# Generated by Django 5.1.5 on 2025-02-08 18:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("shop", "0002_alter_product_options_alter_category_name_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=50, verbose_name="Имя")),
                ("last_name", models.CharField(max_length=50, verbose_name="Фамилия")),
                ("emal", models.EmailField(max_length=254, verbose_name="Почта")),
                ("adress", models.CharField(max_length=250, verbose_name="Адрес")),
                ("postal_code", models.CharField(max_length=20, verbose_name="Индекс")),
                ("city", models.CharField(max_length=100, verbose_name="Город")),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата и время размещения"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Дата и время обновления"
                    ),
                ),
                (
                    "paid",
                    models.BooleanField(default=False, verbose_name="Статус платежа"),
                ),
            ],
            options={
                "verbose_name": "Заказ",
                "verbose_name_plural": "Заказы",
                "ordering": ["-created"],
                "indexes": [
                    models.Index(
                        fields=["-created"], name="orders_orde_created_743fca_idx"
                    )
                ],
            },
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Цена"
                    ),
                ),
                ("count", models.PositiveIntegerField(default=1)),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="orders.order",
                        verbose_name="Заказ",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_items",
                        to="shop.product",
                        verbose_name="Товар",
                    ),
                ),
            ],
        ),
    ]
