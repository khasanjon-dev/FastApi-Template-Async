from typing import Optional

from pydantic import BaseModel


class ProductSchemaBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int


class ProductSchemaCreate(ProductSchemaBase):
    pass


class ProductSchemaUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None


class ProductSchemaRead(ProductSchemaBase):
    id: int

    class Config:
        from_attributes = True
