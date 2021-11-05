from fastapi import APIRouter

from . import lok
from . import accessory
from . import s88
from . import configs

router = APIRouter()
router.include_router(
    lok.router,
    prefix = "/lok",
    tags = ["lok"]
)
router.include_router(
    accessory.router,
    prefix = "/accessory",
    tags = ["accessory"]
)
router.include_router(
    s88.router,
    prefix = "/s88",
    tags = ["s88"]
)
router.include_router(
    configs.router,
    prefix = "/config",
    tags = ["config"]
)