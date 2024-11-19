from abc import ABC, abstractmethod
from typing import Any

import toml


class ConfReader(ABC):
    @abstractmethod
    def read_conf(self, file_path):
        """
        Lire le fichier de configuration
        :param file_path: dossier du fichier de configuration
        """
        pass


class TomlConfReader(ConfReader):
    def read_conf(self, file_path) -> dict[str, Any]:
        """Lire un fichier de configuration écrit au format TOML."""
        with open(file_path, 'r', encoding='unicode_escape') as f:
            return toml.load(f)

    def api_key(self, file_path) -> str:
        """
        Renvoie la clé  API OpenWeatherMap lue depuis le fichier de configuration.

        :param file_path: dossier du fichier de configuration
        :return: la cl  API OpenWeatherMap
        """
        conf = self.read_conf(file_path)
        return conf['api']['weather']['key']
