from fastapi import APIRouter

router = APIRouter(prefix='/char',tags=['character'])

@router.get("/info")
def info():
    pass