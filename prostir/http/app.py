
from fastapi import FastAPI, Request
from prostir.http.easyweek import easyweek_router

app = FastAPI()
app.include_router(easyweek_router)


@app.get("/booking-created")
async def booking_created(request: Request):
    print(await request.json())
    return {"status": 200}


@app.get("/booking-updated")
async def booking_updated(request: Request):
    print(await request.json())
    return {"status": 200}


@app.get("/booking-canceled")
async def booking_canceled(request: Request):
    print(await request.json())
    return {"status": 200}


@app.get("/booking-succeeded")
async def booking_succeeded(request: Request):
    print(await request.json())
    return {"status": 200}
