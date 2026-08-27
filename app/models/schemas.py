from pydantic import BaseModel, Field


class DashboardResponse(BaseModel):
    total_candidates: int = Field(..., ge=0)
    total_applications: int = Field(..., ge=0)
    total_interviews: int = Field(..., ge=0)
    total_offers: int = Field(..., ge=0)
    total_hires: int = Field(..., ge=0)


class FunnelStage(BaseModel):
    stage: str
    count: int = Field(..., ge=0)


class FunnelResponse(BaseModel):
    stages: list[FunnelStage]
