import hmac

from fastapi import APIRouter, Form, Request
from fastapi.responses import FileResponse, RedirectResponse
from pydantic import ValidationError

from app.models import AccessKey
from config import ACCESS_KEY, STATIC_DIR

router = APIRouter()
COOKIE_NAME = "access_key"


def is_valid_key(raw_key: str) -> bool:
    try:
        parsed = AccessKey(key=raw_key)
    except ValidationError:
        return False
    return hmac.compare_digest(parsed.key, ACCESS_KEY)



@router.get("/")
async def login_page(request: Request):
    return FileResponse(rf"{STATIC_DIR}\login.html")


@router.get("/chat")
async def chat_page(request: Request):
    cookie = request.cookies.get(COOKIE_NAME)
    if not cookie or not is_valid_key(cookie):
        return RedirectResponse("/")
    return FileResponse(rf"{STATIC_DIR}\chat.html")


@router.post("/login")
async def login(key: str = Form(...)):
    try:
        AccessKey(key=key)
    except ValidationError:
        return RedirectResponse("/?error=format", status_code=303)

    if not hmac.compare_digest(key, ACCESS_KEY):
        return RedirectResponse("/?error=invalid", status_code=303)

    response = RedirectResponse("/chat", status_code=303)
    response.set_cookie(
        key=COOKIE_NAME,
        value=key,
        httponly=True,
        samesite="lax",
        max_age=60 * 60 * 8,
    )
    return response