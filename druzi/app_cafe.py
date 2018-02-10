from sanic import Sanic
from sanic.response import json, text

from motor.motor_asyncio import AsyncIOMotorClient
uri = 'mongodb://host/my_database'
mongo_connection = AsyncIOMotorClient(uri)
#
# contacts = mongo_connection.mydatabase.contacts

app = Sanic()


@app.route("/")
async def hello(request):
    return text("Hello World!")


@app.post("/login")
async def login(request):
    login = request.form.get('login')
    hash = request.form.get('hash')

    if mongo_connection.CafeEmployee.find_one({'password': {'username': login}}) != hash:
        error = {'error': 'Wrong data provided',
                 'detail': {'field.name': login}}
        return json(error, status=400)

    return json({'token': mongo_connection.CafeEmployee.find_one({'token': {'username': login}})},
                status=200)

#
@app.get('/orders?param=<value>')  #
@app.post('/orders?param=<value>') #
async def orders(request, token):
    if mongo_connection.CafeEmployee.find_one({'username': {'token': token}}) == None:
        error = {'error': 'Wrong API token',
                 'detail': {'field.name': login}}
        return json(error, status=400)

    return json({'orders': mongo_connection.Order}, #
                status=400)


@app.get('/orders/<id>')
async def order(request, token):
    if mongo_connection.CafeEmployee.find_one({'username': {'token': token}}) == None:
        error = {'error': 'Wrong API token',
                 'detail': {'field.name': login}}
        return json(error, status=400)

    elif mongo_connection.Order.find_one({'order': {'order': id}}) == None:
        error = {'error': 'Non-existed order',
                 'detail': {'field.name': login}}
        return json(error, status=400)

    return json(mongo_connection.Order.find_one({'order': id}),
                status=200)

@app.put('/orders/<id>')
async def order(request, token):
    order = request.json
    if mongo_connection.CafeEmployee.find_one({'username': {'token': token}}) == None:
        error = {'error': 'Wrong API token',
                 'detail': {'field.name': login}}
        return json(error, status=400)

    elif mongo_connection.Order.find_one({'order': {'order': order['id']}}) != None:
        error = {'error': 'Existed order with this id',
                 'detail': {'order.id': order['id']}}

        return json(error, status=400)

    insert = await mongo_connection.Order.insert_one(order)
    return json({"The order is inserted with id": str(insert.inserted_id)},
                status=200)


@app.delete('/orders/<id>')
async def order(request, token):
    order = request.json
    if mongo_connection.CafeEmployee.find_one({'username': {'token': token}}) == None:
        error = {'error': 'Wrong API token',
                 'detail': {'field.name': login}}
        return json(error, status=400)

    elif mongo_connection.Order.find_one({'order': {'order': order['id']}}) == None:
        error = {'error': 'Non-existed order',
                 'detail': {'order.id': order['id']}}

        return json(error, status=400)

    mongo_connection.Order.delete_many({'order': order['id']})
    return json({"The order is deleted with id": order['id']},
                status=200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)