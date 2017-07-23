from dppy.behavioral import pubsub
from multiprocessing import Process, SimpleQueue


class MPSubscriber(pubsub.AbsSubscriber):

    def __init__(self, client, worker):
        self._client = client
        self._client.attach(self)
        self.q = SimpleQueue()
        Process(target=worker, args=(self.q,)).start()

    def update(self, o):
        self.q.put(o)

    def __exit__(self, exc_type, exc_value, traceback):
        self._client.detach(self)

