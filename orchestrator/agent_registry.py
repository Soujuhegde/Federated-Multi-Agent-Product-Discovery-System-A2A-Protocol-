import json
from pathlib import Path


class AgentRegistry:

    def __init__(self):

        self.agents = {}

    def load_agent_cards(self):

        card_paths = [
            "youtube_agent/agent_card.json",
            "product_agent/agent_card.json"
        ]

        for card_path in card_paths:

            path = Path(card_path)

            if path.exists():

                with open(path, "r") as f:

                    card = json.load(f)

                self.agents[card["name"]] = card

    def get_agents(self):

        return self.agents