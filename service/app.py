from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from service.routers.items_api import router as items_router
from service.routers.users_api import router as users_router
from service.routers.productsets_api import router as productsets_router
from service.routers.itemvalues_api import router as itemvalues_router

app = FastAPI(title="Pokemon ETB Tracker API")

# CORS (lets your HTML/JS call the API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # for class projects this is fine
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# IMPORTANT: do NOT add prefix here if routers already have their own prefixes
app.include_router(items_router)
app.include_router(users_router)
app.include_router(productsets_router)
app.include_router(itemvalues_router)