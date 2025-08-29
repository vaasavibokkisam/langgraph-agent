# mcp_client.py

def call_common(ability, payload):
    return f"[COMMON executed {ability}] on ticket {payload.get('ticket_id', '')}"

def call_atlas(ability, payload):
    return f"[ATLAS executed {ability}] for {payload.get('customer_name', '')}"

def call_state(ability, payload):
    return f"[STATE updated {ability}]"
