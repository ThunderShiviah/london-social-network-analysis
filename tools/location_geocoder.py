import requests

def geocode_location(location):
    """ Returns a requests response object from the google geocode API.

    Retrieves a response object containing the geocode latitude and longetude for a given location. Also contains other metadata (for more information on requests reponse objects see the requests website: http://docs.python-requests.org/en/). The google geocode API documentation can be found at https://developers.google.com/maps/documentation/geocoding/.

    Args:
        location: A location name.

    Returns:
        A response object that contains a JSON response from the google geocoding API that contains a list of partial matches of location name as well as corresponding location geodata. For example, if r is the response object:

        r.url returns the url API call.
        r.text returns the server's response. 
        r.json() returns the JSON content using the requests' library builtin JSON decoder.

        See the requests documentation (link above) for more examples.
        """

    location = str(location) #FIXME: Should this become a try, except statement? How do I correctly implement ducktyping here?

    payload = {'address': location,
            'region': 'uk'} #For region biasing the API result towards locations in UK.

    url = 'https://maps.googleapis.com/maps/api/geocode/json?'

    r = requests.get(url, params=payload)

    return(r)

