import pandas as pd

class ResponseStrategy:
    """Assuming a successful response, how should we handle
    the incoming data. Examples of concrete ResponseStrategies 
    are:
        . DictResponseStrategy
        . DataFrameResponseStrategy
        . JsonResponseStrategy
    """
    def _follow_path(self, response, path):
        """_follow_path() follows the path (as a file path) 
        into a JSON response and returns the results of the
        requested path.

        Downstream, respond() handles the conversion to the
        strategy type.  
        """
        results = response.json()
        for part in path.split('/'):
            results = results[part]
        return results 


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
        # Follow the path into the response.
        results = self._follow_path(response, path)
        # Send it to DataFrame and return
        results = pd.DataFrame(results)
        return results


class JsonResponseStrategy(ResponseStrategy):
    """Returns the results as a JSON bytes sequence.
    """
    def respond(self, response, path):
        pass