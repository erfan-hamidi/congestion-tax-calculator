# Congestion Tax Calculator

This project is a Django-based application for calculating congestion tax fees for vehicles within specific cities. The application takes into account various rules such as tax-free vehicles, specific time-based tax amounts, and maximum daily tax limits.

## Features

- Calculate congestion tax based on vehicle type and timestamps.
- Different tax rules for different cities.
- Tax-free vehicle types (e.g., Emergency vehicles, Motorbikes, Diplomat vehicles).
- Maximum daily tax limit.
- Supports JSON-based API requests.

## Setup Instructions

### Prerequisites

- Python 3.8+
- Django 3.2+
- Django REST Framework

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/congestion-tax-calculator.git
cd congestion-tax-calculator
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
## API Endpoints
### Calculate Tax:

- POST /api/vehicles/calculate_tax/

#### Request Body:

```json
{
  "vehicle_type": "Car",
  "dates": [
    "2013-02-08T06:20:27",
    "2013-02-08T14:35:00"
  ],
  "city": "Gothenburg"
}
```
#### Response:

```json
{
  "tax": 16
}
```
## Running Tests
To run the tests, execute the following command:

```bash
python manage.py test
```