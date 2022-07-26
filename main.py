from fastapi import FastAPI
from controllers.api import router

app = FastAPI()
app.include_router(router)