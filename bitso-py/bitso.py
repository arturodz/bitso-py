import requests
import time
import hmac
import hashlib

class Bitso:
    def __init__(self, client, key, secret):
        self.client   = client
        self.key      = key
        self.secret   = secret
        self.base_url = 'https://api.bitso.com/v2/'

    def payload(self, kwargs):
        data = {}
        data['key'] = self.key
        nonce = str(int(time.time()))
        msg = nonce + self.client + self.key

        signature = hmac.new(
            self.secret.encode('utf-8'), msg = msg.encode('utf-8'),
            digestmod = hashlib.sha256).hexdigest().upper()
        data['signature'] = signature
        data['nonce'] = nonce

        if kwargs:
            for key in kwargs:
                data[key] = kwargs[key]

        return data

    def public_request(self, action, kwargs):
        r = requests.get(self.base_url + action, data = self.payload(kwargs))
        return r.json()

    def private_request(self, action, kwargs):
        r = requests.post(self.base_url + action, data = self.payload(kwargs))
        return r.json()

    # Public Requests

    def ticker(self, **kwargs):
        return self.public_request('ticker', kwargs)

    def orders(self, **kwargs):
        return self.public_request('orders', kwargs)

    def transactions(self, **kwargs):
        return self.public_request('transactions', kwargs)

    # Private Requests

    def balance(self, **kwargs):
        return self.private_request('balance', kwargs)

    def user_transactions(self, **kwargs):
        return self.private_request('user_transactions', kwargs)

    def open_orders(self, **kwargs):
        return self.private_request('open_orders', kwargs)

    def lookup_order(self, **kwargs):
        return self.private_request('lookup_order', kwargs)

    def orders(self, **kwargs):
        return self.private_request('orders', kwargs)

    def cancel_order(self, **kwargs):
        return self.private_request('cancel_order', kwargs)

    def buy(self, **kwargs):
        return self.private_request('buy', kwargs)

    def sell(self, **kwargs):
        return self.private_request('sell', kwargs)

    def bitcoin_deposit_address(self, **kwargs):
        return self.private_request('bitcoin_deposit_address', kwargs)

    def bitcoin_withdrawal(self, **kwargs):
        return self.private_request('bitcoin_withdrawal', kwargs)

    def ripple_withdrawal(self, **kwargs):
        return self.private_request('ripple_withdrawal', kwargs)
