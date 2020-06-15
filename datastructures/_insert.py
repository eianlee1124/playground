import json
from decimal import Decimal
from pprint import pprint
from sortedcontainers.sorteddict import SortedDict
from websocket import create_connection

ASK = 'asks'
BID = 'bids'
pair = 'BTC/USD'
l2_book = {}


ws = create_connection('wss://ws.kraken.com')
ws.send(json.dumps({
    'event': 'subscribe',
    'pair': [pair],
    'subscription': {
        'name': 'book'
    }
}))

class Price(float):
    __slots__ = ('value')
    
    def __init__(self, value=None):
        self.value = 0.0 or value
    
    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, self.value)
    
class Amount(float):
    __slots__ = ('value')
    
    def __init__(self, value=None):
        self.value = 0.0 or value
    
    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, self.value)

def snapshot(message):
    return SortedDict(
        (Decimal(update[0]), Decimal(update[1]))
        for update in message
    )

while True:
    message = ws.recv()
    if message.startswith('['):
        message = json.loads(message)[1:-2]
        if 'as' in message[0]:
            l2_book[pair] = {
                ASK: snapshot(message[0]['as']),
                BID: snapshot(message[0]['bs'])
            }
        else:
            for msg in message:
                for s, updates in msg.items():
                    side = BID if s == 'b' else ASK
                    for update in updates:
                        price, amount, *_ = update
                        price, amount = Decimal(price), Decimal(amount)
                        if amount == 0:
                            try:
                                del l2_book[pair][side][price]
                            except KeyError:
                                continue
                        else:
                            l2_book[pair][side][price] = amount
            for side in (BID, ASK):
                while len(l2_book[pair][side]) > 10:
                    del_price = l2_book[pair][side].items()[0 if side == BID else -1][0]
                    del l2_book[pair][side][del_price]
    pprint(l2_book, sort_dicts=False)
            
                        
                                
    # for msg in message:
    #     if type(msg) is dict:
    #         if 'as' in msg:
    #             l2_book['asks'] = SortedDict(())
    #             # l2_book['asks'] = SortedDict((price, amount) for price, amount, _ in msg['as'])
    #             # l2_book['bids'] = SortedDict((price, amount) for price, amount, _ in msg['bs'])
    #         else:
    #             for key, orders in msg.items():
    #                 side = BID if key == 'b' else ASK
    #                 for order in orders:
    #                     price, amount, *_ = order

    #                 for price, amount, *_ in orders:
    #                     if float(amount) == 0:
    #                         try:
    #                             l2_book[side].pop(price)
    #                         except KeyError:
    #                             continue
    #                     if float(amount) != 0:
    #                         l2_book[side].update({price: amount})
    #                     while len(l2_book[side]) < 10:
    #                         index = -1 if side == 'asks' else 0
    #                         l2_book[side].popitem(index)
    # pprint(l2_book)
                # asks.update((price, amount) for price, amount, *_ in msg.items())