from bson import ObjectId
from sanic.exceptions import InvalidUsage, Forbidden

from app.models import CafeEmployeeDocument, OrderDocument, CategoryDocument, ProductDocument, CafeDocument


def require_json(func):
    async def wrapped(self, request, **kwargs):
        if request.json is None:
            raise InvalidUsage('Data is not provided.')
        return await func(self, request, **kwargs)

    return wrapped


def check_user(func):
    async def wrapped(self, request, **kwargs):
        token = request.headers.get("token")
        if not token:
            raise InvalidUsage(message='Token is not provided.')

        employee = await CafeEmployeeDocument.find_one({"token": token})
        if not employee:
            raise InvalidUsage(message='Invalid token provided.')
        return await func(self, request, user=employee, **kwargs)

    return wrapped


async def check_user_cafe(user, order_id):
    order = await OrderDocument.find_one({"_id": ObjectId(order_id)})
    if order.cafe != user.cafe:
        raise Forbidden(message="You don't have access to this order.")
    return order


def check_bot(func):
    async def wrapped(self, request, **kwargs):
        token = request.headers.get("token")
        if not token:
            raise InvalidUsage(message='Token is not provided.')

        return await func(self, request, **kwargs)

    return wrapped


async def make_order_with_products(order_data):
    products = []
    for product_id in order_data.get('products'):
        product = await ProductDocument.find_one({"_id": ObjectId(product_id)})
        if product:
            products.append(product.dump())
    order_data['products'] = products
    return order_data


async def find_document_by_field(document, field_name, field_value):
    pass


async def check_cafe_name(name):
    cafe = await CafeDocument.find_one({"name": name})
    if not cafe:
        raise Forbidden(message="There is no cafe with that name.")
    # cafe = await CafeDocument.find_one({"name": name})
    return cafe.dump()


async def get_all_categories(name):
    cafe = await check_cafe_name(name)
    categories_cursor = CategoryDocument.find({"cafe": ObjectId(cafe['id'])})
    categories = [category.dump() async for category in categories_cursor]

    return categories


async def get_category_by_id(name, category_id):
    cafe = await check_cafe_name(name)
    category = await CategoryDocument.find_one({"_id": ObjectId(category_id), "cafe": ObjectId(cafe['id'])})
    if category:
        return category.dump()
    raise Forbidden(message="There is no category with that id.")


# async def get_all_products(name):
#     categories = await get_all_categories(name)
#     products = []
#
#     print(categories)
#
#     for category in categories:
#         products_cursor = ProductDocument.find({"category": ObjectId(category['id'])})
#         products.append(product.dump() async for product in products_cursor)
#
#     return products
#
#
#
# async def get_product_by_id(name, product_id):
#     categories = await get_all_categories(name)
#
#     print(categories)
#
#     for category in categories:
#         product = ProductDocument.find_one({"_id": ObjectId(product_id), "category": ObjectId(category['id'])})
#         if product:
#             return product
#
#     # products = get_all_products(name)
#     # product = products[]
#
#     raise Forbidden(message="There is no product with that id.")
