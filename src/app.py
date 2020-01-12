from starlette.applications import Starlette
from starlette.responses    import JSONResponse
from starlette.routing      import Route
from starlette.graphql      import GraphQLApp
import uvicorn

from database import init_db
from schema import schema

async def helloworld(request):
    return JSONResponse({'hello': 'world'})

routes = [
    Route('/', helloworld),
    Route('/graphql', GraphQLApp(schema=schema))
    ]

app = Starlette(debug=True, routes=routes)

if __name__ == '__main__':
    init_db()
    uvicorn.run(app, host="0.0.0.0", port=8000)