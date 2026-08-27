"""Dashboard service for recruitment KPIs and funnel metrics.

This service intentionally isolates temporary sample data from the rest of the
application so it can later be replaced with database queries or a data pipeline
without changing the API surface.
"""

from app.models.schemas import DashboardResponse, FunnelResponse, FunnelStage


class DashboardService:
    """Provides dashboard metrics using temporary sample values until real data integration is ready."""

    def get_dashboard_summary(self) -> DashboardResponse:
        """Return the recruitment KPI summary for the dashboard."""
        return DashboardResponse(
            total_candidates=1200,
            total_applications=980,
            total_interviews=520,
            total_offers=180,
            total_hires=120,
        )

    def get_funnel_data(self) -> FunnelResponse:
        """Return funnel counts ordered from application to hire."""
        stages = [
            FunnelStage(stage="Applied", count=1200),
            FunnelStage(stage="Screening", count=950),
            FunnelStage(stage="Interview", count=520),
            FunnelStage(stage="Offer", count=180),
            FunnelStage(stage="Hired", count=120),
        ]
        return FunnelResponse(stages=stages)
