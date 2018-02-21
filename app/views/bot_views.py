import uuid

from sanic.exceptions import Forbidden, InvalidUsage
from sanic.response import json, text
from sanic.views import HTTPMethodView

from app.models import CafeDocument, CafeEmployeeDocument, CategoryDocument
from app.serializers import AuthSerializer, OrderSerializer
from app.utils import (require_json, check_user, check_user_cafe,
                       make_order_with_products, check_cafe_name, check_bot, get_all_categories, get_category_by_id,
                       get_all_products, get_product_by_id)


class IndexView(HTTPMethodView):
    async def get(self, request):
        return text("ok")


class CafesView(HTTPMethodView):
    @check_bot
    async def get(self, request):
        cafes_cursor = CafeDocument.find({})
        cafes = [cafe.dump() async for cafe in cafes_cursor]

        return json({"cafes": cafes}, status=200)


class CafesByNameView(HTTPMethodView):
    @check_bot
    async def get(self, request, name):
        cafe = await check_cafe_name(name)

        return json({"cafe": cafe}, status=200)


class CategoriesView(HTTPMethodView):
    @check_bot
    async def get(self, request, name):

        return json({"categories": await get_all_categories(name)}, status=200)


class CategoriesByIdView(HTTPMethodView):
    @check_bot
    async def get(self, request, name, category_id):

        return json({"category": await get_category_by_id(name, category_id)}, status=200)



class ProductsView(HTTPMethodView):
    # @check_bot
    async def get(self, request, name):

        return json({"products": await get_all_products(name)}, status=200)



#
# class ProductsByIdView(HTTPMethodView):
#     @check_bot
#
# class CheckoutView(HTTPMethodView):
#     @check_bot
