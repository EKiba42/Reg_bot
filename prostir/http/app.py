
from fastapi import FastAPI
from prostir.http.easyweek import easyweek_router

app = FastAPI()
app.include_router(easyweek_router)
