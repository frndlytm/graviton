class Putter:
    def respond(self, url):
        raise NotImplementedError

class NullPutter(Putter):
    def respond(self, url):
        return None