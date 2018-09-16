"""
@name: grav.core.getters
@auth: frndlytm@github.com
"""
import requests
import pandas as pd

from core.exceptions import FailedRequestError


class Getter:
    """Handles getting data from a target REST url, following
    a path into the data as necessary. 
    
    A concrete Getter is also responsible for converting the 
    reponse data into the configured type. 
    
    This could potentially be decorated, and path following 
    could be the primary responsibility of the Getter.
    """
    def _follow_path(self, response, path):
        """_follow_path() follows the path (as a file path) 
        into a JSON response and returns the results of the
        requested path.

        Downstream, respond() handles the conversion to the
        strategy type.  
        """
        for part in path.split('/'):
            results = results[part]
        return results 


    def respond(self, url, path):
        """respond() returns the data from the response using
        the concrete response type.

        Given a response and requested path to the results in
        the reponse, gets the results.
        """
        response = requests.get(url)

        # On successful attempts...
        if 200 <= response.status_code < 300:
            return response.json()

        # On failed attempts...
        else:
            raise FailedRequestError(
                response.status_code, url,
                'could not be gotten. Consult API documentation.'
            )



class NullGetter(Getter):
    """Returns None"""
    def response(self, url, path):
        return None


class DictGetter(Getter):
    """Returns the results from a reponse in the Python
    standard dictionary form.
    """
    def respond(self, url, path):
        return super().respond(url, path)



class DataFrameGetter(Getter):
    """Returns the results from a response in a DataFrame
    format.
    """
    def respond(self, url, path):
        # Get as far as the parent
        response = super().respond(url, path)
        # Follow the path into the response.
        results = self._follow_path(response, path)
        # Send it to DataFrame and return
        results = pd.DataFrame(results)
        return results


class TextGetter(Getter):
    """Returns the results as a string.
    """
    def respond(self, url, path):
        response = super().respond(url, path)
        results = self._follow_path(response, path)
        return str(results)