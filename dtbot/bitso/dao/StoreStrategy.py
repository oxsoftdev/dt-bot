class StoreStrategy:

    def __init__(self, store):
        self.store = store

    def insert_stream_update(self, o):
        StreamUpdate_id = self.store.ws.insert_stream_update(o)
        for _o in o.payload:
            if isinstance(_o, OrderUpdate):
                self.store.ws.insert_order_update(StreamUpdate_id, _o)
            elif isinstance(_o, TradeUpdate):
                self.store.ws.insert_trade_update(StreamUpdate_id, _o)
