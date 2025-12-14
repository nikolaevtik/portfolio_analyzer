from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routers import portfolio
import os
from dotenv import load_dotenv

load_dotenv()  # загружаем переменные окружения

app = FastAPI(
    title=os.getenv("APP_NAME", "Анализатор портфеля"),
    debug=os.getenv("DEBUG", "False").lower() == "true"
)

# Подключаем статические файлы (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Подключаем шаблоны
templates = Jinja2Templates(directory="templates")

# Подключаем роутеры
app.include_router(portfolio.router, prefix="/portfolio")

@app.get("/")
async def root(request: Request):
    """Главная страница"""
    return templates.TemplateResponse(
        "index.html", 
        {"request": request, "title": "Анализатор портфеля"}
    )