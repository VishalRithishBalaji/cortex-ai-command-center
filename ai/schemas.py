from pydantic import BaseModel


class DecisionReport(BaseModel):

    incident_type: str

    confidence: float

    severity: int

    affected_population: int

    traffic_impact: str

    environmental_impact: str

    recommended_department: str

    estimated_repair_cost: int

    estimated_repair_time_days: int

    priority: str

    executive_summary: str

    recommended_action: str