from pydantic import BaseModel, Field


class BlueprintRequest(BaseModel):
    """What the business owner sends to us."""

    business_description: str = Field(min_length=20, max_length=2000)


class AgentSpec(BaseModel):
    """One agent inside the blueprint."""

    name: str = Field(min_length=1, max_length=60)
    role: str = Field(min_length=1, max_length=300)
    tools: list[str] = Field(default_factory=list)


class AgentBlueprint(BaseModel):
    """The full plan we generate."""

    title: str = Field(min_length=1, max_length=100)
    summary: str = Field(min_length=1, max_length=500)
    agents: list[AgentSpec] = Field(min_length=1)