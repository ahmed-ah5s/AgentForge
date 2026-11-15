import pytest
from pydantic import ValidationError

from app.schemas.blueprint import AgentBlueprint, AgentSpec, BlueprintRequest


def test_valid_request():
    request = BlueprintRequest(
        business_description="We run a small online shop and need help with support."
    )

    assert request.business_description.startswith("We run")


def test_short_description_is_rejected():
    with pytest.raises(ValidationError):
        BlueprintRequest(business_description="too short")


def test_blueprint_needs_at_least_one_agent():
    with pytest.raises(ValidationError):
        AgentBlueprint(
            title="Support plan",
            summary="Help customers",
            agents=[],
        )


def test_tools_default_to_empty_list():
    agent = AgentSpec(
        name="Support Agent",
        role="Answers customer questions",
    )

    assert agent.tools == []