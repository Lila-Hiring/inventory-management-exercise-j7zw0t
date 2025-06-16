from fastapi import APIRouter
from scalar_fastapi import get_scalar_api_reference

from ._architectures import router as architectures_router
from ._computers import router as computers_router
from ._cpus import router as cpus_router
from ._manufacturers import router as manufacturers_router
from ._operating_systems import router as operating_systems_router

# Router for all routes we want to expose under the `/v1` API path.
v1_router = APIRouter(prefix="/v1")

v1_router.include_router(computers_router)
v1_router.include_router(architectures_router)
v1_router.include_router(cpus_router)
v1_router.include_router(manufacturers_router)
v1_router.include_router(operating_systems_router)


@v1_router.get("/docs", include_in_schema=True)
def scalar_html():
    return get_scalar_api_reference(
        openapi_url="/v1/openapi.json",
        title="inventory_management_exercise",
    )
