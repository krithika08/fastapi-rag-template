from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
def status():
    return {"status": "running"}
@router.get("/health")
def health_check():
    return {"status": "ok", "source": "copier update"}

