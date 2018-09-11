import pandas as pd

class ResponseStrategy:
    """Assuming a successful response, how should we handle
    the incoming data. Examples of concrete ResponseStrategies 
    are:
        . DictResponseStrategy
        . DataFrameResponseStrategy
        . JsonResponseStrategy
    """
    def respond(self, response, path):
        """respond() returns the data from the response using
        the concrete response type.

        Given a response and requested path to the results in
        the reponse, gets the results.
        """
        raise NotImplementedError


class DictResponseStrategy(ResponseStrategy):
    """Returns the results from a reponse in the Python
    standard dictionary form.
    """
    def respond(self, response, path):
        pass


class DataFrameResponseStrategy(ResponseStrategy):
    """Returns the results from a response in a DataFrame
    format.
    """
    def respond(self, response, path):
        # Assume the path is like a file path
        path = path.split('/')

        # Using the response, traverse the path
        # incrementally 
        results = response.json()
        for item in path:
            results = results[item]

        # Send it to DataFrame and return
        results = pd.DataFrame(results)
        return results


class JsonResponseStrategy(ResponseStrategy):
    """Returns the results as a JSON bytes sequence.
    """
    def respond(self, response, path):
        pass