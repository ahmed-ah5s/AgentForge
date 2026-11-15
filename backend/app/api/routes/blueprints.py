from typing import Annotated

from fastapi import APIRouter, Depends

from app.providers.base import BlueprintProvider
from app.providers.mock import MockBlueprintProvider
from app.schemas.blueprint import AgentBlueprint, BlueprintRequest

router = APIRouter(prefix="/blueprints", tags=["Blueprints"])


def get_blueprint_provider() -> BlueprintProvider:
    return MockBlueprintProvider()


@router.post("", response_model=AgentBlueprint)
async def create_blueprint(
    request: BlueprintRequest,
    provider: Annotated[BlueprintProvider, Depends(get_blueprint_provider)],
) -> AgentBlueprint:
    return await provider.generate_blueprint(request)