from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.secret_key = 'sm_mail_hub_premium_key'

# SMTP কনফিগারেশন (এখানে আপনার জিমেইল সেটআপ হবে পরে)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'your-email@gmail.com' 
app.config['MAIL_PASSWORD'] = 'your-app-password'   
app.config['MAIL_DEFAULT_SENDER'] = 'your-email@gmail.com'

mail = Mail(app)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        data = request.json
        msg = Message(
            subject=data.get('subject'),
            recipients=[data.get('recipient')],
            body=data.get('message')
        )
        mail.send(msg)
        return jsonify({"status": "success", "message": "Email sent successfully!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
