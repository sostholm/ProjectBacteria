from starlette.applications import Starlette
from starlette.responses    import JSONResponse
from starlette.routing      import Route

async def helloworld(request):
    return JSONResponse({'hello': 'world'})

routes = [Route('/', helloworld)]

app = Starlette(debug=True, routes=routes)