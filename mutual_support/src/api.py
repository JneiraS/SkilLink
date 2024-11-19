from abc import ABC, abstractmethod

import requests


class APImanager(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def fetch_data(self):
        """
        Renvoie les données de la réponse de l'API.
        Le contenu des données renvoyées dépend de l'API.
        """
        pass


class WeatherAPI(APImanager):
    """
    Classe permettant de communiquer avec l'API OpenWeatherMap.
    """

    def __init__(self, city, api_key):
        self.city = city
        self.api_key = api_key

    def fetch_data(self) -> dict | None:
        """
        Récupère les données de prévisions météorologiques de l'API OpenWeatherMap pour la ville spécifiée.
        Renvoie le contenu de la réponse sous la forme d'un dictionnaire JSON, ou None en cas d'erreur.
        """
        api_url = "https://api.openweathermap.org/data/2.5/forecast"
        query_params = {
            "q": self.city,
            "appid": self.api_key,
            "units": "metric",
            "lang": "fr",
            "exclude": "hourly,minutely,current,alerts"
        }
        try:
            response = requests.get(api_url, params=query_params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as error:
            print(f"Error during OpenWeatherMap API request: {error}")
            return None

    @staticmethod
    def get_rainy_days(data) -> set:
        """
        Renvoie un ensemble de dates au format 'AAAA-MM-JJ' pour lesquelles il est prévu de la pluie.
        Les dates sont extraites de la réponse de l'API OpenWeatherMap.
        """
        if data is None:
            return set()

        return set([c['dt_txt'][:10] for c in data['list'] if c['weather'][0]['main'] == 'Rain'])
