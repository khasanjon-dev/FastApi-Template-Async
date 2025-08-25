from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.config.database import get_db_session
from backend.app.models.products import Product
from backend.app.schemas.products import (
    ProductSchemaRead,
    ProductSchemaCreate,
    ProductSchemaUpdate,
)

router = APIRouter(prefix="/products", tags=["products"])


@router.post(
    "/",
    response_model=ProductSchemaRead,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new product",
    description="Creates a new product and returns the created product with its ID.",
)
async def create_product(
    product: ProductSchemaCreate, db: AsyncSession = Depends(get_db_session)
):
    db_product = Product(**product.dict())
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product


@router.get(
    "/",
    response_model=List[ProductSchemaRead],
    summary="List products",
    description="Retrieves a paginated list of products.",
)
async def read_products(
    offset: int = 0,
    limit: int = 5,
    db: AsyncSession = Depends(get_db_session),
):
    stmt = select(Product).order_by(Product.id).offset(offset).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()


@router.get(
    "/{product_id}",
    response_model=ProductSchemaRead,
    summary="Get a product by ID",
    description="Retrieves a single product by its ID. Returns 404 if not found.",
)
async def read_product(product_id: int, db: AsyncSession = Depends(get_db_session)):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )
    return product


@router.put(
    "/{product_id}",
    response_model=ProductSchemaRead,
    summary="Update a product by ID",
    description="Updates all fields of a product (full update). Returns 404 if not found.",
)
async def update_product(
    product_id: int,
    product: ProductSchemaUpdate,
    db: AsyncSession = Depends(get_db_session),
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    db_product = result.scalar_one_or_none()
    if not db_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )

    for key, value in product.dict(exclude_unset=True).items():
        setattr(db_product, key, value)

    await db.commit()
    await db.refresh(db_product)
    return db_product


@router.delete(
    "/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a product by ID",
    description="Deletes the product with the given ID. Returns 204 No Content if successful.",
)
async def delete_product(
    product_id: int,
    db: AsyncSession = Depends(get_db_session),
):
    result = await db.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )

    await db.delete(product)
    await db.commit()
    return  # ✅ 204 No Content, no response body
