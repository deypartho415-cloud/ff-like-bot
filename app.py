from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import time

app = Flask(__name__)
CORS(app)

# আপনার সেই ১টি সচল টোকেন এখানে সেট করা আছে
GUEST_TOKEN = "il+xU1ll5m+j1YGZ1RlUldqWE+w3upSQpNe3hMVaLX53EA=="

@app.route('/like', methods=['POST'])
def send_like():
    data = request.get_json()
    uid = data.get('uid')
    
    if not uid:
        return jsonify({"message": "সঠিক UID দিন!"}), 400
        
    success_count = 0
    garena_api_url = "https://freefiremobile.com"
    
    headers = {
        "Authorization": f"Bearer {GUEST_TOKEN}",
        "Content-Type": "application/json",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; Build/RP1A.201005.011)"
    }
    
    payload = {
        "target_uid": int(uid),
        "source": 1
    }
    
    # এই লুপটি আপনার ওই একটি টোকেন ব্যবহার করেই গেম সার্ভারে ৫০ বার লাইক রিকোয়েস্ট পাঠাবে
    for i in range(50):
        try:
            response = requests.post(garena_api_url, json=payload, headers=headers, timeout=5)
            if response.status_code == 200:
                success_count += 1
            time.sleep(0.1) # সার্ভার ব্লকিং এড়াতে সামান্য বিরতি
        except Exception as e:
            continue
            
    if success_count > 0:
        return jsonify({"message": f"অনুরোধ সফল! আপনার ওই অ্যাকাউন্ট থেকে {success_count} বার লাইক প্রসেস করা হয়েছে।"})
    else:
        return jsonify({"message": "গেম সার্ভার সাড়া দিচ্ছে না। অনুগ্রহ করে নতুন করে টোকেন সংগ্রহ করুন।"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
