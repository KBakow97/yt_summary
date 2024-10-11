from fastapi import FastAPI, Request
from routers.youtube import router_youtube

app = FastAPI()

app.include_router(router_youtube)