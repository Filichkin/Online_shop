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
