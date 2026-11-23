import os

from fastapi import APIRouter, Form, Request
from fastapi.responses import FileResponse, RedirectResponse, JSONResponse
from pydantic import ValidationError

from app.models import AccessKey, ChatMessage
from app.llm_requests import make_request
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


async def ask_llm(message: str) -> str:
    llm_response = make_request(message)

    if llm_response:
        try:
            data = llm_response["choices"][0]["message"]["content"]
        except Exception:
            data = "Error while extracting LLM response."

    else:
        data = "Error during the LLM API request."

    return data


@router.post("/chat/send")
async def send_message(request: Request, message: str = Form(...)):
    access_cookie = request.cookies.get("access_key")
    if not access_cookie == ACCESS_KEY:
        return JSONResponse(status_code=401, content={"error": "Unauthorized"})

    try:
        ChatMessage(message=message)
    except ValidationError:
        return JSONResponse(status_code=400, content={"error": "Invalid message"})

    try:
        reply = await ask_llm(message)
    except Exception:
        return JSONResponse(status_code=500, content={"error": "Failed to get a response from the model"})

    return JSONResponse(content={"reply": reply})
