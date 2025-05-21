# 🧠 FastAPI CSV Backend for Real-Time Agent Simulation

This is a standalone FastAPI backend designed to simulate a real-time conversational agent system. It handles tickets, leads, bookings, and messages using **CSV files** as persistent storage—ideal for quick prototyping, internal tools, or integration with agent frameworks like **LangGraph**.

---

## 🚀 Features

✅ Fully functional FastAPI server  
✅ Endpoints strictly follow provided HTML API spec  
✅ CSV-based persistence: No external database needed  
✅ Clean, documented Python code  
✅ Independently runnable without LangGraph or other agents  

---

## 📋 Implemented Endpoints

| Method | Endpoint                         | Description                      |
|--------|----------------------------------|----------------------------------|
| GET    | `/check-status`                  | Check server status              |
| POST   | `/{user_id}/make_ticket`         | Create a new ticket              |
| GET    | `/{user_id}/get_ticket_info`     | Retrieve ticket info for a user  |
| POST   | `/{user_id}/create_lead`         | Create a lead                    |
| POST   | `/{user_id}/make_booking`        | Create a booking                 |
| GET    | `/fetch_slots`                   | Fetch available booking slots    |
| POST   | `/send_sms`                      | Simulate sending an SMS          |
| POST   | `/confirm_registration`          | Confirm a booking registration   |

All routes perform input validation and respond with structured JSON responses as described in the spec.

---

## 📂 File Structure

├── main.py # FastAPI application
├── requirements.txt # Dependencies
├── README.md # Project documentation
├── users.csv # User records
├── leads.csv # Leads data
├── tickets.csv # Tickets data
└── bookings.csv # Bookings data



---

## 🔧 Setup & Run

1. **Install dependencies**
    pip install -r requirements.txt

2 **Run the server**
   uvicorn main:app --reload

3 **Visit docs**

    Swagger UI: http://localhost:8000/docs

    ReDoc: http://localhost:8000/redoc

    Testing 
    curl http://localhost:8000/check-status




# 🧠 FastAPI CSV Backend for Real-Time Agent Simulation

This is a standalone FastAPI backend designed to simulate a real-time conversational agent system. It handles tickets, leads, bookings, and messages using **CSV files** as persistent storage—ideal for quick prototyping, internal tools, or integration with agent frameworks like **LangGraph**.

---

## 🚀 Features

✅ Fully functional FastAPI server  
✅ Endpoints strictly follow provided HTML API spec  
✅ CSV-based persistence: No external database needed  
✅ Clean, documented Python code  
✅ Independently runnable without LangGraph or other agents  

---

## 📋 Implemented Endpoints

| Method | Endpoint                         | Description                      |
|--------|----------------------------------|----------------------------------|
| GET    | `/check-status`                  | Check server status              |
| POST   | `/{user_id}/make_ticket`         | Create a new ticket              |
| GET    | `/{user_id}/get_ticket_info`     | Retrieve ticket info for a user  |
| POST   | `/{user_id}/create_lead`         | Create a lead                    |
| POST   | `/{user_id}/make_booking`        | Create a booking                 |
| GET    | `/fetch_slots`                   | Fetch available booking slots    |
| POST   | `/send_sms`                      | Simulate sending an SMS          |
| POST   | `/confirm_registration`          | Confirm a booking registration   |

All routes perform input validation and respond with structured JSON responses as described in the spec.

---

## 🏗️ Project Structure

