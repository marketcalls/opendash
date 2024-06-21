from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import date
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///default.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Flask-SQLAlchemy
db = SQLAlchemy(app)

# Models
class Stock(db.Model):
    __tablename__ = 'stocks'
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(128), nullable=False)
    last_price = db.Column(db.Float, nullable=False)
    last_update = db.Column(db.Date, nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

# Database initialization function
def init_db():
    db.create_all()  # Creates all tables
    if not Stock.query.count():
        stocks = [
            Stock(symbol='AAPL', name='Apple Inc.', last_price=145.09, last_update=date(2023, 6, 19)),
            Stock(symbol='GOOGL', name='Alphabet Inc.', last_price=2729.89, last_update=date(2023, 6, 19)),
            Stock(symbol='AMZN', name='Amazon.com, Inc.', last_price=3450.00, last_update=date(2023, 6, 19)),
            Stock(symbol='MSFT', name='Microsoft Corporation', last_price=299.35, last_update=date(2023, 6, 19)),
        ]
        db.session.bulk_save_objects(stocks)
        db.session.commit()

@app.route('/')
def index():
    api_message = os.getenv('FLASK_STOCK_MARKET_DASHBOARD_API', 'Flask Stock Market Dashboard API')
    return f'<h1>{api_message}</h1>'

@app.route('/api/stocks')
def api_stocks():
    stocks = [stock.as_dict() for stock in Stock.query.all()]
    return jsonify(stocks)

# Call the setup function at application startup within the app context
with app.app_context():
    init_db()

if __name__ == '__main__':
    app.run(debug=True)
