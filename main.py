from fastapi import FastAPI, Request, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routers.youtube import router_youtube
from fastapi.responses import HTMLResponse

app = FastAPI()

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # lub ["*"], aby zezwolić na wszystkie połączenia
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Obsługa statycznych plików
app.mount("/static", StaticFiles(directory="static"), name="static")

# Ustawienie templates directory
templates = Jinja2Templates(directory="templates")

# Dodajemy router YouTube
app.include_router(router_youtube)
