import urequests, ujson

URL = "yourusername.pythonanywhere.com"
PASS = "your_secure_password"
# Change this ID to start a fresh "memory" block on the server
SESSION_ID = "tdeck_user_v1"

def ask_ai(question):
    headers = {"Authorization": PASS, "Content-Type": "application/json"}
    payload = ujson.dumps({"query": question, "session_id": SESSION_ID})
    
    try:
        res = urequests.post(URL, data=payload, headers=headers)
        if res.status_code == 200:
            print("AI:", res.json().get("answer"))
        else:
            print("Server Error:", res.status_code)
        res.close()
    except Exception as e:
        print("Network Error:", e)
