import requests
import time

BOT_TOKEN = "8435760656:AAFsmGdidpMJwquiGg--Lzt0hDobJMTG13w"
CHAT_ID = "8166130855"
URL = "https://www.myntra.com/sale"   # Update to the page where coupon appears

def send_telegram(msg):
    api_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(api_url, data={"chat_id": CHAT_ID, "text": msg})

def check_coupon():
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(URL, headers=headers, timeout=10)

    if "Blinkdeal" in r.text:
        send_telegram("🚨 Blinkdeal coupon is ACTIVE on Myntra!")
    else:
        print("Coupon not active yet.")

if __name__ == "__main__":
    # Run every 10 minutes
    while True:
        check_coupon()
        time.sleep(600)   # 600 sec = 10 mins
