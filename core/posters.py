class Poster:
    def respond(self, url):
        raise NotImplementedError

class NullPoster(Poster):
    def respond(self, url):
        return None