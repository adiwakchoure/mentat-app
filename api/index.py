from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import os
import sys

load_dotenv()  # take environment variables from .env.
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from routes import router
from models import Query, UrlRelevance


import marvin
marvin.settings.openai.api_key = os.getenv('OPENAI_API_KEY')

app = FastAPI()
app.include_router(router)

async def exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=400,
        content={"message": str(exc)},
    )

@app.get("/api/health")
def read_env():
    result = marvin.classify("no", labels=bool)
    return {"Status": "OK"}