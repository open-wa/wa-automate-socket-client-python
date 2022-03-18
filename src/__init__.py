import json
import re
import time
import uuid

import requests
import socketio
from socketio.exceptions import ConnectionError

__version__ = '1.0.0'


class SocketClient(object):
    def __init__(self, url, api_key=None, sync=True):
        """
        :param url: wa-automate URL
        :param api_key: Authentication key (required if provided on wa-automate cli initialization)
        :param sync: Default sync/async behavior
        """
        self.handlers = {}
        self.url = re.sub('\/$', '', url)
        self.sync = sync

        self.io = socketio.Client()

        @self.io.event
        def connect():
            self.io.emit("register_ev")

        @self.io.on('*')
        def catch_all(event, data):
            event = event.split('.')[0]
            if event in self.handlers:
                for handler in self.handlers[event].values():
                    handler(data)

        @self.io.event
        def connect_error(data):
            print(data)

        while True:
            try:
                self.io.connect(self.url, auth={'apiKey': api_key})
                break
            except ConnectionError:
                time.sleep(5)

    def __dir__(self):
        self.methods = json.loads(requests.get(self.url + '/meta/basic/commands').content.decode())
        self.on_events = json.loads(requests.get(self.url + '/meta/basic/listeners').content.decode())
        methods = list(self.methods.keys()) + self.on_events + super().__dir__()
        methods.sort()
        return methods

    def __getattr__(self, item):
        client = self

        class Func:
            def __call__(self, *args, **kwargs):
                if item.startswith('on'):
                    client.listen(item, args[0])
                else:
                    sync = client.sync
                    if 'sync' in kwargs:
                        sync = kwargs['sync']

                    if sync:
                        return client.io.call(item, {'args': args})
                    else:
                        cb = kwargs['callback'] if 'callback' in kwargs else lambda _: None
                        client.io.emit(item, {'args': args}, callback=cb)

        return Func()

    def stop_listener(self, listener, listener_id):
        if listener in self.handlers and listener_id in self.handlers[listener]:
            del self.handlers[listener][listener_id]
            return True
        return False

    def listen(self, event, handler):
        id = str(uuid.uuid4())
        if event not in self.handlers:
            self.handlers[event] = {}
        self.handlers[event][id] = handler
        return id

    def disconnect(self):
        self.io.disconnect()
