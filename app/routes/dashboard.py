from fastapi import APIRouter

from app.models.schemas import DashboardResponse, FunnelResponse
from app.services.dashboard_service import DashboardService


router = APIRouter(prefix="/api")
service = DashboardService()


@router.get("/dashboard", response_model=DashboardResponse)
def get_dashboard() -> DashboardResponse:
    """Return overall recruitment KPIs for the dashboard."""
    return service.get_dashboard_summary()


@router.get("/funnel", response_model=FunnelResponse)
def get_funnel() -> FunnelResponse:
    """Return ordered recruitment stages and counts for the funnel chart."""
    return service.get_funnel_data()
