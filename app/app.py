from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.dashboard import router as dashboard_router


app = FastAPI(
    title="HR Recruitment Analytics API",
    description="Backend API for recruitment funnel metrics and dashboard insights.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dashboard_router)


@app.get("/health")
def health_check() -> dict[str, str]:
    """Simple health endpoint used by local development and deployment checks."""
    return {"status": "healthy"}
