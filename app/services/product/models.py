from tortoise import fields
from tortoise.models import Model


class Product(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=80, unique=True)
    sku_id = fields.CharField(max_length=10, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)
