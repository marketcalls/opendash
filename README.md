# OpenDash - Stock Market Dashboard

Welcome to OpenDash, a Flask-based Stock Market Dashboard application. This app provides an API to fetch stock data and displays a welcoming message on the home route.

## Features

- Fetch stock data through a RESTful API
- Display a custom welcome message
- Initialize the database with sample stock data

## Technologies Used

- Python 3.11
- Flask 3.0.3
- Flask-SQLAlchemy 3.0.3
- SQLite
- python-dotenv 1.0.1

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.11
- pip (Python package installer)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/marketcalls/opendash
    cd opendash
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory and add the following:

    ```env
    FLASK_STOCK_MARKET_DASHBOARD_API="Welcome to OpenDash"
    DATABASE_URL="sqlite:///default.db"
    ```

    Alternatively, you can use the provided `.sample.env` as a template:

    ```bash
    cp .sample.env .env
    ```

5. **Initialize the database:**

    ```bash
    flask shell
    from app import init_db
    init_db()
    exit()
    ```

### Running the Application

To start the Flask development server:

```bash
flask run
