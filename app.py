from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/api/contact', methods=['POST'])
def contact():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        if not name or not email or not message:
            return jsonify({"status": "error", "message": "All fields are required!"}), 400

        print(f"\n📩 New Message from {name} ({email})")
        print(f"Message: {message}\n")

        return jsonify({
            "status": "success", 
            "message": f"Thank you {name}! Your message has been received."
        })
    except:
        return jsonify({"status": "error", "message": "Server error"}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
