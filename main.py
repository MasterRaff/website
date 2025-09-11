from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request
import uvicorn

app = FastAPI()

# Mount the "static" folder to serve files like CSS, JS, images, etc.
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve index.html at root
@app.get("/")
async def read_index():
    return FileResponse("static/index.html")

# Custom 404 handler
@app.exception_handler(404)
async def not_found(request: Request, exc):
    return FileResponse("static/404.html", status_code=404)
if __name__ == "__main__":
    uvicorn.run(
            "main:app",       # points to app inside server.py
        host="0.0.0.0",     # accessible from outside
        port=8000,
        reload=True         # auto-reload on code changes (great for dev)
    )
