from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field
from typing import Optional, List
import csv
import os
from datetime import datetime

app = FastAPI()

# File paths
USERS_CSV = 'users.csv'
LEADS_CSV = 'leads.csv'
TICKETS_CSV = 'tickets.csv'
BOOKINGS_CSV = 'bookings.csv'

# Ensure CSV files exist
def ensure_csv(file, headers):
    if not os.path.exists(file):
        with open(file, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)

ensure_csv(USERS_CSV, ['user_id', 'name', 'email'])
ensure_csv(LEADS_CSV, ['user_id', 'lead_id', 'product', 'interested'])
ensure_csv(TICKETS_CSV, ['user_id', 'ticket_id', 'issue', 'status'])
ensure_csv(BOOKINGS_CSV, ['user_id', 'booking_id', 'slot', 'confirmed'])

# Models
class TicketRequest(BaseModel):
    issue: str = Field(..., min_length=5)

class TicketResponse(BaseModel):
    ticket_id: str
    status: str

class LeadRequest(BaseModel):
    product: str
    interested: bool

class LeadResponse(BaseModel):
    lead_id: str

class BookingRequest(BaseModel):
    slot: str

class BookingResponse(BaseModel):
    booking_id: str
    confirmed: bool

class SMSRequest(BaseModel):
    phone_number: str
    message: str

# Helper functions
def write_csv(file, data):
    with open(file, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)

def read_csv(file):
    with open(file, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)

# Routes
@app.get("/check-status")
def check_status():
    return {"status": "Server is running"}

@app.post("/{user_id}/make_ticket", response_model=TicketResponse)
def make_ticket(user_id: str = Path(...), request: TicketRequest = ...):
    ticket_id = f"TKT{int(datetime.utcnow().timestamp())}"
    write_csv(TICKETS_CSV, [user_id, ticket_id, request.issue, 'open'])
    return TicketResponse(ticket_id=ticket_id, status='open')

@app.get("/{user_id}/get_ticket_info", response_model=List[TicketResponse])
def get_ticket_info(user_id: str = Path(...)):
    tickets = read_csv(TICKETS_CSV)
    user_tickets = [TicketResponse(ticket_id=t['ticket_id'], status=t['status'])
                    for t in tickets if t['user_id'] == user_id]
    return user_tickets

@app.post("/{user_id}/create_lead", response_model=LeadResponse)
def create_lead(user_id: str = Path(...), request: LeadRequest = ...):
    lead_id = f"LEAD{int(datetime.utcnow().timestamp())}"
    write_csv(LEADS_CSV, [user_id, lead_id, request.product, request.interested])
    return LeadResponse(lead_id=lead_id)

@app.post("/{user_id}/make_booking", response_model=BookingResponse)
def make_booking(user_id: str = Path(...), request: BookingRequest = ...):
    booking_id = f"BK{int(datetime.utcnow().timestamp())}"
    write_csv(BOOKINGS_CSV, [user_id, booking_id, request.slot, False])
    return BookingResponse(booking_id=booking_id, confirmed=False)

@app.get("/fetch_slots")
def fetch_slots():
    return {"available_slots": ["10:00", "11:00", "14:00", "15:00"]}

@app.post("/send_sms")
def send_sms(sms: SMSRequest):
    # Simulate SMS sending
    return {"message": f"SMS sent to {sms.phone_number}"}

@app.post("/confirm_registration")
def confirm_registration(user_id: str = Query(...), booking_id: str = Query(...)):
    bookings = read_csv(BOOKINGS_CSV)
    updated = False
    with open(BOOKINGS_CSV, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['user_id', 'booking_id', 'slot', 'confirmed'])
        writer.writeheader()
        for row in bookings:
            if row['user_id'] == user_id and row['booking_id'] == booking_id:
                row['confirmed'] = 'True'
                updated = True
            writer.writerow(row)
    if not updated:
        raise HTTPException(status_code=404, detail="Booking not found")
    return {"message": "Registration confirmed"}
