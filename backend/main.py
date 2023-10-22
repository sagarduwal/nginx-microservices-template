from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from router import api_router

app = FastAPI()

app.include_router(api_router)

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html(req: Request):
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="Custom API docs",
        oauth2_redirect_url=req.url_for("oauth2_redirect"),
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )

@app.get("/openapi.json", include_in_schema=False)
async def get_open_api_endpoint():
    return get_openapi(title="Custom API", version=1, routes=app.routes)
