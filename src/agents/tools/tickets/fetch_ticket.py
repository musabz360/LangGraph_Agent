# fetch_ticket.py
# ---------------------------
# Dummy support ticket fetcher.
# Intended for testing ticket‐listing behavior.

def fetch_ticket() -> list:
    """
    Returns a list of support tickets (dummy data).
    """
    # Simulated tickets with ID and status
    return [
        {"ticket_id": "TCKT-1001", "status": "open"},
        {"ticket_id": "TCKT-1002", "status": "closed"},
    ]
