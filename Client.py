import requests
import time
import json
from telegram import Bot
import asyncio

HEIMDALL_API = "https://heimdall-api-amoy.polygon.technology/checkpoints/latest"  # Example API endpoint
# BOR_API = "http://localhost:1317/bor/latest-span"            # Example API endpoint

# telegram_bot_token = "7123503158:AAEp78SxtjpCQplPRmz9zjN3_aMcu7qHh78"
# telegram_chat_id = "https://api.telegram.org/bot7123503158:AAEp78SxtjpCQplPRmz9zjN3_aMcu7qHh78/getUpdates"
with open('config.json') as f:
    config = json.load(f)

def fetch_block_height(api):
    try:
        response = requests.get(api)
        response.raise_for_status()
        block_info = response.json()
        return block_info['height']
    except Exception as e:
        print(f"Error fetching height from {api}: {e}")
        return None

def send_alert(message):
    # Function to send alert via Telegram
    try:
        bot = Bot(token=config['telegram_bot_token'])
        asyncio.run(bot.send_message(chat_id=config['telegram_chat_id2'], text=message))
        print(f"Alert sent: {message}")
    except Exception as e:
        print(f"Failed to send alert: {e}")

def main():
    while True:
        heimdall_height = fetch_block_height(HEIMDALL_API)
        bor_height = 0

        if heimdall_height is not None and bor_height is not None:
            print(f"Heimdall Height: {heimdall_height}, Bor Height: {bor_height}")

            # Alert if heights are out of sync
            if heimdall_height != bor_height:
                send_alert("Alert")
                # Trigger alerting mechanism here

        time.sleep(10)  # Polling interval

if __name__ == "__main__":
    main()