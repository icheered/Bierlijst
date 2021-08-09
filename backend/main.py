import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.api.api import api_router
from src.utils.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup():
    """Perform some logic on startup"""
    pass


@app.on_event("shutdown")
def shutdown():
    """Perform some logic on shutdown"""
    pass


app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
