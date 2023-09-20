from datetime import datetime

from fastapi import APIRouter
from pydantic import BaseModel


easyweek_router = APIRouter(
    prefix="/easyweek",
    tags=["easyweek"],
    responses={404: {"description": "Not found"}},
)


class BookingModel(BaseModel):
    id: int
    user_name: str
    service_name: str
    location_lat: float
    location_lng: float
    location_address_formatted: str
    customer_full_name: str
    customer_phone: str
    customer_id: int
    booking_date_start: datetime
    booking_date_start_formatted: str
    booking_duration_formatted: str
    booking_price_formatted: str


@easyweek_router.post("/booking-canceled", tags=["easyweek"])
async def booking_canceled(booking_info: BookingModel):
    return print(booking_info)


@easyweek_router.post("/booking-updated", tags=["easyweek"])
async def booking_updated(booking_info: BookingModel):
    return print(booking_info)


@easyweek_router.post("/booking-created", tags=["easyweek"])
async def booking_created(booking_info: BookingModel):
    return print(booking_info)
