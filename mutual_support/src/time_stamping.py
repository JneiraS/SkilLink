from abc import ABC, abstractmethod
from datetime import datetime, timedelta

from mutual_support.src.api import APImanager


class TimeStamp(ABC):
    pass

    @abstractmethod
    def is_expired(self):
        """
        Vérifie si l'horodatage est expiré.
        Returns: bool: Retourne True si l'horodatage est expiré, False sinon.
        """
        pass


class APITimestamp(TimeStamp):
    """
    Classe permettant de gérer l'horodatage d'une API.
    """
    def __init__(self, api_manager: APImanager):
        self.stamp = datetime.now()
        self.api_manager = api_manager
        self.data = self.api_manager.fetch_data()

    def is_expired(self) -> bool:
        current_time = datetime.now()
        return (current_time - self.stamp) > timedelta(minutes=10)

    def get_data(self) -> dict:
        """
        Renvoie les données de l'API.
        """
        if self.is_expired():
            self.data = self.api_manager.fetch_data()
        return self.data
