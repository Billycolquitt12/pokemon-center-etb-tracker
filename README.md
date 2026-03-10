# Pokemon ETB Tracker

## Overview
Pokemon ETB Tracker is a multi-tier application built using Python, FastAPI, MySQL, and an HTML/JavaScript client. The system tracks Pokémon ETB items and supports creating, viewing, and updating records through a web client and API.

## Technologies Used
- Python
- FastAPI
- MySQL
- HTML
- JavaScript

## Project Structure
- `client/` - HTML front end
- `service/` - FastAPI service layer
- `business/` - business logic
- `dao/` - database access layer
- `createtables.sql` - database schema
- `insertdata.sql` - sample data

## Setup Instructions

### 1. Database Setup
Run the following SQL scripts in MySQL Workbench:
- `createtables.sql`
- `insertdata.sql`

### 2. Install Dependencies
pip install fastapi uvicorn mysql-connector-python
3. Start the API
python -m uvicorn service.app:app --reload

Open Swagger at:
http://127.0.0.1:8000/docs

4. Run the Client

Open the HTML client in a browser.

## Features

Create item

Get all items

Get item by ID

Update item

Delete item (if enabled)

##Testing

The application was tested end-to-end through the HTML client, FastAPI service, and MySQL database.
