from fastapi import APIRouter

api_router = APIRouter(prefix="/api")

@api_router.get("/")
def read_status():
    return {"status": "OK"}

@api_router.get("/version")
def read_version():
    return {"version": "0.1.0"}