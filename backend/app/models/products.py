from typing import Optional

from sqlalchemy import String, Float, Integer
from sqlalchemy.orm import mapped_column, Mapped

from backend.app.utils.database import BaseDB, BaseTimeStamp


class Product(BaseDB, BaseTimeStamp):
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(255))
    price: Mapped[float] = mapped_column(Float, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, default=0)
