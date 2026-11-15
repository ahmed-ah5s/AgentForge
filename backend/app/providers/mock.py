from app.providers.base import BlueprintProvider
from app.schemas.blueprint import (
    AgentBlueprint,
    AgentSpec,
    BlueprintRequest,
)


class MockBlueprintProvider(BlueprintProvider):
    """Mock provider that returns a predefined customer support blueprint."""

    async def generate_blueprint(
        self,
        request: BlueprintRequest,
    ) -> AgentBlueprint:
        return AgentBlueprint(
            title="Customer Support Automation",
            summary=(
                "An AI-powered customer support system "
                "that helps businesses answer customer questions."
            ),
            agents=[
                AgentSpec(
                    name="Customer Support Agent",
                    role="Answers customer questions and manages support requests.",
                    tools=[
                        "knowledge_base_search",
                        "create_support_ticket",
                    ],
                )
            ],
        )