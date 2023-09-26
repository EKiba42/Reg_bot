from sqlalchemy import MetaData, Table, Column, Integer, String, Float, Null, DateTime

metadate = MetaData()

users = Table(
    "users",
    metadate,
    Column("id", Integer, primary_key=True),
    Column("phone", String),
    Column("chat_id", Integer, nullable=False),
    Column("customer_id", Integer, nullable=True),
)

bookings = Table(
     "bookings",
     metadate,
     Column("id", Integer, primary_key=True),
     Column("user_name", String, nullable=False),
     Column("service_name", String, nullable=False),
     Column("location_lat", Float, nullable=False),
     Column("location_lng", Float, nullable=False),
     Column("location_address_formatted", String, nullable=False),
     Column("customer_full_name", String, nullable=False),
     Column("customer_phone", String, nullable=False),
     Column("customer_id", Integer, nullable=False),
     Column("booking_date_start", DateTime, nullable=False),
     Column("booking_date_start_formatted", String, nullable=False),
     Column("booking_duration_formatted", String, nullable=False),
     Column("booking_price_formatted", String, nullable=False),
)
