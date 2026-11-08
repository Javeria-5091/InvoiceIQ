from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health():
    """Used by humans, Docker and monitoring tools to check the app is alive."""
    return {"status": "ok"}
