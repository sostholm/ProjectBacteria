from starlette.applications import Starlette
from starlette.responses    import JSONResponse
from starlette.routing      import Route
from starlette.graphql      import GraphQLApp
from starlette.middleware   import Middleware
import uvicorn

from database import init_db
from schema import schema
from timermiddleware import TimerMiddleware


async def helloworld(request):
    return JSONResponse({'hello': 'world'})

routes = [
    Route('/', helloworld),
    Route('/graphql', GraphQLApp(schema=schema))
    ]

middleware = [
    Middleware(TimerMiddleware)
]

app = Starlette(debug=True, routes=routes, middleware=middleware)

if __name__ == '__main__':
    # init_db()
    uvicorn.run(app, host="0.0.0.0", port=8000)