from sqlalchemy import MetaData, Table, Column, Integer, String, Float, Null, TIMESTAMP

metadate = MetaData()

users = Table(
    "users",
    metadate,
    Column("id", Integer, primary_key=True),
    Column("number", String),
    Column("chat_id", Integer),
    Column("customer_id", Integer, nullable=True),
)

bookings = Table(
     "bookings",
     metadate,
     Column("id", Integer),
     Column("user_name", String, nullable=False),
     Column("service_name", String),
     Column("location_lat", Float),
     Column("location_lng", Float),
     Column("location_address_formatted", String),
     Column("customer_full_name", String),
     Column("customer_phone", String),
     Column("customer_id", Integer),
     Column("booking_date_start", TIMESTAMP),
     Column("booking_date_start_formatted", String),
     Column("booking_duration_formatted", String),
     Column("booking_price_formatted", String),
)
