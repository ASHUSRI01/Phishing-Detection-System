from flask import Flask, request, jsonify, render_template
import pickle
import os
from extraction import detect_input_type
from logger import log_request, log_error

app = Flask(__name__, static_folder='static', template_folder='templates')

MODEL_PATH = 'phishing_model.pkl'
model = pickle.load(open(MODEL_PATH, 'rb'))

# --- Home Page ---
@app.route("/")
def index():
    return render_template("index.html")

# --- Serve Forms via GET ---
@app.route("/url-check", methods=["GET"])
def url_check_page():
    return render_template("url-check.html")

@app.route("/email-check", methods=["GET"])
def email_check_page():
    return render_template("email-check.html")

# --- Handle POST submissions from JS ---
@app.route("/url-check", methods=["POST"])
def check_url():
    data = request.get_json()
    url = data.get('url', '')
    if not url:
        return jsonify(status='error', message='Enter a URL'), 400

    if detect_input_type(url) != 'url':
        return jsonify(status='warning', message='Invalid URL')

    try:
        pred = model.predict([url])[0]  
        status = 'danger' if pred == 1 else 'safe'
        msg = 'Phishing' if pred else 'Legitimate'
        log_request('URL', url, status)
        return jsonify(status=status, message=msg)
    except Exception as e:
        log_error('URL', url, str(e))
        return jsonify(status='error', message='Server error'), 500

@app.route("/email-check", methods=["POST"])
def check_email():
    data = request.get_json()
    email = data.get('email', '')
    if not email:
        return jsonify(status='error', message='Enter email text'), 400

    if detect_input_type(email) != 'email':
        return jsonify(status='warning', message='Invalid email text')

    try:
        pred = model.predict([email])[0]
        status = 'danger' if pred == 1 else 'safe'
        msg = 'Phishing' if pred else 'Legitimate'
        log_request('Email', email[:30], status)
        return jsonify(status=status, message=msg)
    except Exception as e:
        log_error('Email', email, str(e))
        return jsonify(status='error', message='Server error'), 500

if __name__ == "__main__":
    os.makedirs("logs", exist_ok=True)
    app.run(debug=True)
