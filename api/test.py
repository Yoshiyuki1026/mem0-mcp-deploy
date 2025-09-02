from starlette.applications import Starlette
from starlette.responses import JSONResponse

app = Starlette()

@app.route("/")
async def homepage(request):
    return JSONResponse({"message": "Hello Vercel!"})

@app.route("/test")
async def test_endpoint(request):
    return JSONResponse({"status": "working", "path": "/test"})