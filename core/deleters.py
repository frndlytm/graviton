class Deleter:
    def respond(self, url):
        raise NotImplementedError

class NullDeleter(Deleter):
    def respond(self, url):
        return None