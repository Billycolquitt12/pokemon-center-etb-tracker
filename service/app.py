from fastapi import FastAPI

from service.routers.items_api import router as items_router
from service.routers.users_api import router as users_router
from service.routers.productsets_api import router as productsets_router
from service.routers.itemvalues_api import router as itemvalues_router

app = FastAPI(title="Pokemon ETB Tracker API")

# No prefix here because each router file has its own prefix
app.include_router(items_router)
app.include_router(users_router)
app.include_router(productsets_router)
app.include_router(itemvalues_router)