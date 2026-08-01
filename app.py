from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/like', methods=['POST'])
def send_like():
    data = request.get_json()
    uid = data.get('uid')
    if not uid:
        return jsonify({"message": "সঠিক UID দিন!"}), 400
    
    # ফ্রি লাইক এপিআই লিংক
    api_url = f"https://vercel.app{uid}"
    try:
        response = requests.get(api_url, timeout=15)
        if response.status_code == 200:
            return jsonify({"message": f"UID: {uid} তে লাইক পাঠানো হয়েছে!"})
        else:
            return jsonify({"message": "সার্ভার ব্যস্ত, পরে চেষ্টা করুন।"})
    except Exception as e:
        return jsonify({"message": "সার্ভারে সমস্যা হয়েছে।"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)