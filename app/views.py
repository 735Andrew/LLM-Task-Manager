import os

from fastapi import APIRouter, Form, Request
from fastapi.responses import FileResponse, RedirectResponse
from pydantic import ValidationError

from app.models import AccessKey
from config import ACCESS_KEY, STATIC_DIR

router = APIRouter()


@router.get("/")
async def login_page():
    return FileResponse(os.path.join(STATIC_DIR, "login.html"))


@router.post("/login")
async def login(key: str = Form(...)):
    try:
        AccessKey(key=key)
    except ValidationError:
        return RedirectResponse("/?error=format", status_code=303)

    if not key == ACCESS_KEY:
        return RedirectResponse("/?error=invalid", status_code=303)

    response = RedirectResponse("/chat", status_code=303)
    response.set_cookie(
        key="access_key",
        value=ACCESS_KEY,
        httponly=True,
        samesite="lax",
    )
    return response


@router.get("/chat")
async def chat_page(request: Request):
    access_cookie = request.cookies.get("access_key")
    if not access_cookie == ACCESS_KEY:
        return RedirectResponse("/")

    return FileResponse(os.path.join(STATIC_DIR, "chat.html"))
