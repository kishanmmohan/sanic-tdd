from sanic.response import HTTPResponse, json


async def list_products(request) -> HTTPResponse:
    return json(dict(test="test"))
