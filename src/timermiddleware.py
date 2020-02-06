from starlette.middleware.base import BaseHTTPMiddleware
import time

class TimerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        tic = time.perf_counter()
        response = await call_next(request)
        toc = time.perf_counter()
        print(f'{round(toc-tic, 2)}s')
        return response