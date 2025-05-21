# book_appointment.py
# ---------------------------
# Dummy “book appointment” endpoint—in real use, this would persist data
# and send confirmations via email/SMS.

def book_appointment() -> str:
    """
    Books an appointment (dummy implementation).
    """
    # Always returns a fixed confirmation message for testing
    return "Thank you! Your appointment has been successfully booked for 10:00 PM."
