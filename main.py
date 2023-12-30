from fastapi import FastAPI

from users import router

app = FastAPI()
app.include_router(router)