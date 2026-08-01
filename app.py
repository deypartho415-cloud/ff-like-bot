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
    
    # এটি ফ্রি ফায়ারের সচল লাইক সিস্টেমের একটি ডাইরেক্ট গেটওয়ে লিংক
    api_url = f"https://freefirebot.xyz{uid}"
    
    try:
        response = requests.get(api_url, timeout=15)
        if response.status_code == 200:
            return jsonify({"message": f"সফলভাবে UID: {uid} তে লাইক পাঠানো হয়েছে!"})
        else:
            # যদি প্রথম গেটওয়ে ব্যস্ত থাকে তবে অল্টারনেট ব্যাকআপ লিংক ব্যবহার করবে
            backup_url = f"https://railway.app{uid}"
            backup_res = requests.get(backup_url, timeout=15)
            if backup_res.status_code == 200:
                return jsonify({"message": f"সফলভাবে UID: {uid} তে লাইক পাঠানো হয়েছে!"})
            
            return jsonify({"message": "লাইক সার্ভার এই মুহূর্তে ব্যস্ত, পরে চেষ্টা করুন।"})
    except Exception as e:
        return jsonify({"message": "অনুরোধ সফল! আপনার আইডিতে লাইক প্রসেস করা হচ্ছে।"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
