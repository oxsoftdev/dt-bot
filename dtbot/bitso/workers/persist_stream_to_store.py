from ..dao import StoreStrategy


def worker(store):
    def _worker(q):
        while True:
            if not q.empty():
                o = o.get()
                StoreStrategy(store).insert_stream_update(o)
    return _worker

