import json, urllib
from decimal import Decimal
from websocket import create_connection
import everpay

def get_amount_out(user, order, token_out_tag):
    amount_out = 0
    for path in order['paths']:
        if path['to'].lower() == user.lower() and path['tokenTag'] == token_out_tag:
            amount_out += int(path['amount'])
    return str(amount_out)
    
class Permaswap:
    def __init__(self, router_host, account):
        self.router_url = urllib.parse.urljoin(router_host, '/wsuser')
        self.account = account
    
    def get_order(self, token_in, token_out, amount_in):
        token_in_tag = self.account.get_token_tag(token_in)
        token_out_tag = self.account.get_token_tag(token_out)
        token_in_decimals = self.account.get_token(token_in).decimals
        token_out_decimals = self.account.get_token(token_out).decimals
        query = {
            'event': 'query',
            'address': self.account.address,
            'tokenIn': token_in_tag,
            'tokenOut': token_out_tag,
            'amountIn': str(amount_in)
        }
        ws = create_connection(self.router_url)
        ws.send(json.dumps(query))
        order = json.loads(ws.recv())
        if order['event'] == 'order':
            order['tokenIn'] = token_in_tag
            order['tokenOut'] = token_out_tag
            order['amount_in'] = str(amount_in)
            order['amount_out'] = get_amount_out(self.account.address, order, token_out_tag)
            order['amount_in2'] = str(Decimal(int(order['amount_in']))/Decimal(10**token_in_decimals))
            order['amount_out2'] = str(Decimal(int(order['amount_out']))/Decimal(10**token_out_decimals))
            order['rate'] = float(order['amount_out2'])/float(order['amount_in2'])
            return order
    
    def place_order(self, order):
        bundle = everpay.load_bundle(order)
        sig = self.account.sign_bundle(bundle.get_data_to_sign())
        bundle.add_sig(self.account.address, sig)
        submit_order = {
            'event': 'submit',
            'address': self.account.address,
            'tokenIn': order['tokenIn'],
            'tokenOut': order['tokenOut'],
            'bundle': json.loads(bundle.get_data())['bundle'],
            'paths': order['paths']
        }
        ws = create_connection(self.router_url)
        ws.send(json.dumps(submit_order))
        data = ws.recv()
        data = json.loads(data)
        return data