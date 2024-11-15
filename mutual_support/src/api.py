from abc import ABC, abstractmethod

import requests


class APImanager(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def _fetch_data(self):
        """
        Returns data from the API response.
        The content of the returned data depends on the API.
        """
        pass


class WeatherAPI(APImanager):
    """
    Classe permettant de communiquer avec l'API OpenWeatherMap.
    """

    def __init__(self, city, api_key):
        self.city = city
        self.api_key = api_key

    def _fetch_data(self):
        """
        Effectue une requête sur l'API OpenWeatherMap pour obtenir
        les prévisions métoreologiques pour la ville spécifiée.
        Renvoie le contenu de la réponse sous forme de dictionnaire
        JSON.
        """
        url = f"https://api.openweathermap.org/data/2.5/forecast"
        params = {
            "q": self.city,
            "appid": self.api_key,
            "units": "metric",
            "lang": "fr",
            "exclude": "hourly,minutely,current,alerts"
        }
        # API request
        with requests.get(url, params=params) as response:
            response.raise_for_status()
            return response.json()

    def get_rainy_days(self):
        """
        Renvoie un ensemble de dates au format 'AAAA-MM-JJ' pour lesquelles il est prévu de la pluie.
        Les dates sont extraites de la réponse de l'API OpenWeatherMap.
        """
        data = self._fetch_data()
        return set([c['dt_txt'][:10] for c in data['list'] if c['weather'][0]['main'] == 'Rain'])





