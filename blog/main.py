from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from db import models
from db.database import engine
from router import post

app = FastAPI()

# Routers
app.include_router(post.router)

# Database
models.Base.metadata.create_all(engine)

# Static files
app.mount('/images', StaticFiles(directory="images"), name="images")

# Allow cross-origin requests
origins = [
    'http://localhost:3000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Exception handler
@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    """ HTTPException handler """
    return JSONResponse(
        status_code=404,
        content={'details': exc, 'type': "HTTPException"}
    )