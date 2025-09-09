from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

bookings = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/bookings', methods=['GET'])
def get_bookings():
    return jsonify([booking.strftime('%Y-%m-%d') for booking in bookings])

@app.route('/api/book', methods=['POST'])
def book():
    data = request.json
    booking_date = datetime.strptime(data['date'], '%Y-%m-%d')
    # check the date
    today = datetime.now()
    if today <= booking_date < today + timedelta(days=7):
        return jsonify({"error": "Bookings must be made at least one week in advance."}), 400

    bookings.append(booking_date)
    return jsonify({"message": "Booking successful!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
