from fastapi import FastAPI

from routers.access_tokens import router as access_tokens_router
from routers.current_user import router as current_user_router
from routers.gocd import router as gocd_router
from routers.health import router as health_router
from routers.jobs import router as jobs_router
from routers.materials import router as materials_router
from routers.pipelines import router as pipelines_router
from routers.users import router as users_router

app = FastAPI(
    title="GoCD",
    version="25.3.0",
    servers=[
        {"url": "https://gocd.polacoproject.net", "description": "Remote server"},
        {"url": "http://localhost:8080", "description": "Local server"},
    ],
)

app.include_router(access_tokens_router)
app.include_router(current_user_router)
app.include_router(gocd_router)
app.include_router(health_router)
app.include_router(jobs_router)
app.include_router(materials_router)
app.include_router(pipelines_router)
app.include_router(users_router)
