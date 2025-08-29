import json
import logging
import os
from mcp_client import call_common, call_atlas, call_state

# Setup logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/agent.log",
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_and_print(message):
    """Helper to print and log at the same time"""
    print(message)
    logging.info(message)

# Load config.json
with open("config.json", "r") as f:
    config = json.load(f)

# Load dataset.json
with open("dataset.json", "r") as f:
    dataset = json.load(f)

log_and_print("\n🚀 Starting LangGraph Agent Execution...\n")

# Process each ticket
for ticket in dataset:
    log_and_print(f"\n=====================")
    log_and_print(f"🎫 Processing Ticket ID: {ticket['ticket_id']}")
    log_and_print("=====================\n")

    state = ticket.copy()

    for stage in config["stages"]:
        stage_name = stage["name"]
        mode = stage["mode"]
        abilities = stage.get("abilities", [])

        log_and_print(f"➡️ Stage {stage['id']}: {stage_name} ({mode})")

        for ability in abilities:
            if "mcp_map" in stage:
                mcp = stage["mcp_map"].get(ability, "COMMON")
            else:
                mcp = stage.get("mcp", "COMMON")

            # Call the correct MCP stub
            if mcp == "COMMON":
                result = call_common(ability, state)
            elif mcp == "ATLAS":
                result = call_atlas(ability, state)
            elif mcp == "STATE":
                result = call_state(ability, state)
            else:
                result = f"[Unknown MCP {mcp}]"

            state[f"{stage_name.lower()}_{ability}"] = result
            log_and_print(f"   ⚡ {result}")

        log_and_print(f"   ✅ State after stage {stage_name}: {state}\n")

    log_and_print("🎯 Final Payload Output for Ticket:")
    log_and_print(json.dumps(state, indent=2))
    log_and_print("\n----------------------------------------------------\n")

