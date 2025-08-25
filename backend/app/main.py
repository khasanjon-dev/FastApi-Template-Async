import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.app.config.core import settings
from backend.app.config.database import sessionmanager
from backend.app.routers.products import router as products_router
from backend.app.utils.database import BaseDB

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s — %(message)s",
)
logger = logging.getLogger("lifespan")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up: creating DB tables if not exist")
    async with sessionmanager._engine.begin() as conn:
        await conn.run_sync(BaseDB.metadata.create_all)

    yield

    logger.info("Shutting down: disposing DB engine")
    await sessionmanager.close()


app = FastAPI(title=settings.PROJECT_NAME, lifespan=lifespan)

app.include_router(products_router, prefix=settings.API_V1_STR)
