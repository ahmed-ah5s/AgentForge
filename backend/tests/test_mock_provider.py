import asyncio

from app.providers.mock import MockBlueprintProvider
from app.schemas.blueprint import AgentBlueprint, BlueprintRequest


def test_mock_provider_generates_blueprint():
    provider = MockBlueprintProvider()

    request = BlueprintRequest(
        business_description=(
            "We need an AI agent to answer customer questions."
        )
    )

    blueprint = asyncio.run(provider.generate_blueprint(request))

    assert isinstance(blueprint, AgentBlueprint)
    assert blueprint.title == "Customer Support Automation"
    assert len(blueprint.agents) == 1
    assert blueprint.agents[0].name == "Customer Support Agent"


def test_mock_provider_generates_expected_tools():
    provider = MockBlueprintProvider()

    request = BlueprintRequest(
        business_description=(
            "We need an AI agent to answer customer questions."
        )
    )

    blueprint = asyncio.run(provider.generate_blueprint(request))

    assert blueprint.agents[0].tools == [
        "knowledge_base_search",
        "create_support_ticket",
    ]