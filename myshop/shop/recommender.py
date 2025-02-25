import redis
from django.conf import settings

from .models import Product


REDIS = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.DEDIS_DB
)


class Recommender:
    def get_product_key(self, id):
        return f'product:{id}:purchased_with'

    def products_bouth(self, products):
        product_ids = [product.id for product in products]
        for product_id in product_ids:
            for with_id in product_ids:
                if product_id != with_id:
                    REDIS.zincrby(
                        self.get_product_key(product_id),
                        1,
                        with_id
                    )

    def suggest_products_for(self, products, max_results=6):
        product_ids = [product.id for product in products]
        if len(products) == 1:
            suggestions = REDIS.zrange(
                self.get_product_key(product_ids[0]), 0, -1, desc=True
            )[:max_results]
        else:
            flat_ids = ''.join([str(id) for id in product_ids])
            temporary_key = f'tmp_{flat_ids}'
            keys = [self.get_product_key(id) for id in product_ids]
            REDIS.zunionstore(temporary_key, keys)
            REDIS.zrem(temporary_key, *product_ids)
            suggestions = REDIS.zrange(
                temporary_key, 0, -1, desc=True
            )[:max_results]
            REDIS.delete(temporary_key)
            suggested_products_ids = [int(id) for id in suggestions]
            suggested_products = list(
                Product.objects.filter(id__in=suggested_products_ids)
            )
            suggested_products.sort(
                key=lambda x: suggested_products_ids.index(x.id)
            )
            return suggested_products

    def clear_purchases(self):
        for id in Product.objects.values_list('id', flat=True):
            REDIS.delete(self.get_product_key(id))
