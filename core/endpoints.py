"""
@name: grav.core.endpoints
@auth: frndlytm@github.com
"""
class EndpointBuilder:
    """EndpointFactories build templates for Endpoints
    from configuration dictating required parameters
    and default values.
    """
    def build(self, config):
        pass

class Endpoint:
    """Endpoints permit an Api to get() data from them
    and are contained in a dictionary in the Api class
    by their name. They have a template, built by their
    builder, to 
    """
    def __init__(self, name, template):
        self.name = name
        self.template = template

    def get_name(self):
        return self.name

    def render(self, params):
        self.template.render(params)

