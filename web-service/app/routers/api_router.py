from fastapi import APIRouter
from .bollinger_bands import bollinger_bands_router
from .isolation_forest import isolation_forest_router
from .dbscan import dbscan_router

router = APIRouter()

# Agrega las rutas de los enrutadores específicos
router.include_router(
    bollinger_bands_router, 
    prefix="/bollinger-bands", 
    tags=["bollinger-bands"],
    responses={404: {"description": "Not found"}}
)
router.include_router(
    isolation_forest_router, 
    prefix="/isolation-forest", 
    tags=["isolation-forest"],
    responses={404: {"description": "Not found"}}
)
router.include_router(
    dbscan_router, 
    prefix="/dbscan", 
    tags=["dbscan"],
    responses={404: {"description": "Not found"}}
)
