from app.views import cafe_views, bot_views

namespaces = [
    {"name": "/cafe",
     "routes": [{"handler": cafe_views.IndexView, "path": "/"},
                {"handler": cafe_views.LoginView, "path": "/login/"},
                {"handler": cafe_views.OrdersView, "path": "/orders/"},
                {"handler": cafe_views.OrdersByIdView, "path": "/orders/<order_id>/"}]
     },
    {"name": "/bot",
     "routes": [{"handler": bot_views.IndexView, "path": "/"},
                {"handler": bot_views.CafesView, "path": "/cafes/"},
                {"handler": bot_views.CafesByNameView, "path": "/cafes/<name>/"},
                {"handler": bot_views.CategoriesView, "path": "/cafes/<name>/categories"},
                {"handler": bot_views.CategoriesByIdView, "path": "/cafes/<name>/categories/<category_id>"},
                {"handler": bot_views.ProductsView, "path": "/cafes/<name>/products"}
                # {"handler": bot_views.ProductsByIdView, "path": "/cafes/<name>/products/<product_id>"},
                # {"handler": bot_views.CheckoutView, "path": "/checkout/"}]
     ]
     }
]


def add_routes(app):
    for namespace in namespaces:
        name = namespace.get('name')
        routes = namespace.get('routes')
        for route in routes:
            app.add_route(route.get('handler').as_view(), f"{name}{route.get('path')}")
