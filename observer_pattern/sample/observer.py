class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print("{} got message '{}'".format(self.name, message))


class Publisher:
    def __init__(self, events):
        # initialize usisng a dictionary comprehension
        self.subscribers = { event : dict() for event in events }

    def get_subscribers(self, event):
        # returns a dictionary of subscribers
        return self.subscribers[event]

    def register(self, event, who, callback=None):
        # callback takes into account scenarios where the update method is called something else
        if callback is None:
            # callback is not supplied. Default to using the update method
            callback = getattr(who, 'update')
        self.get_subscribers(event)[who] = callback

    def unregister(self, event, who):
        del self.get_subscribers(event)[who]

    def dispatch(self, event, message):
        for subscriber, callback in self.get_subscribers(event).items():
            callback(message)
