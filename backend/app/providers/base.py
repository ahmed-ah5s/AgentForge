from typing import Protocol

from app.schemas.blueprint import AgentBlueprint, BlueprintRequest


class BlueprintProvider(Protocol):
    """Interface for generating agent blueprints."""

    async def generate_blueprint(
        self,
        request: BlueprintRequest,
    ) -> AgentBlueprint:
        ...