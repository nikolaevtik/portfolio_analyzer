from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# Пока используем временное хранилище в памяти
fake_portfolio = []

@router.get("/")
async def show_portfolio(request: Request):
    """Показать портфель"""
    return templates.TemplateResponse(
        "portfolio.html",
        {"request": request, "portfolio": fake_portfolio}
    )

@router.post("/add")
async def add_ticker(ticker: str = Form(...)):
    """Добавить тикер в портфель"""
    fake_portfolio.append({"ticker": ticker.upper(), "price": 0})
    return RedirectResponse("/portfolio", status_code=303)

@router.get("/clear")
async def clear_portfolio():
    """Очистить портфель"""
    fake_portfolio.clear()
    return RedirectResponse("/portfolio", status_code=303)