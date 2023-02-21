import requests
import time
from datetime import datetime
from plyer import notification

# Set the target cryptocurrency and currency for comparison
crypto_currency = 'BTC'
fiat_currency = 'USD'

# Set the API URL for real-time price tracking
api_url = f'https://api.coinmarketcap.com/v1/ticker/{crypto_currency}/?convert={fiat_currency}'

def get_crypto_price():
    response = requests.get(api_url)
    response_json = response.json()
    price_in_fiat = response_json[0]['price_' + fiat_currency.lower()]
    return float(price_in_fiat)

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='CryptoTracker',
        timeout=10
    )

if __name__ == '__main__':
    target_price = float(input('Enter your target price for Bitcoin (in USD): '))
    while True:
        crypto_price = get_crypto_price()
        date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'{date_time} - Current {crypto_currency}/{fiat_currency} price: {crypto_price:.2f}')
        if crypto_price > target_price:
            send_notification(title=f'{crypto_currency} Price Alert',
                              message=f'Current {crypto_currency}/{fiat_currency} price: {crypto_price:.2f}')
            break
        time.sleep(60)
