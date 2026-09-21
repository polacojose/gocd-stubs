from fastapi import Depends, FastAPI
from routers.pipelines import router as pipelines_router

from common import Tags, bearer, verify_accept_header_v2
from routers.jobs import router as jobs_router

app = FastAPI()

app.include_router(jobs_router)
app.include_router(pipelines_router)
