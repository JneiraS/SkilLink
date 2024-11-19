from unittest.mock import patch

import pytest

from mutual_support.src.conf_reader import TomlConfReader


@pytest.fixture
def conf_reader():
    return TomlConfReader()


@pytest.fixture(autouse=True)
def mock_api_key(monkeypatch):
    conf = {'api': {'weather': {'key': 'test'}}}
    with patch('mutual_support.src.conf_reader.toml.load', return_value=conf):
        yield


class TestConfReader:
    def test_read_conf(self, conf_reader):
        assert conf_reader.api_key('./../../../conf.toml') == 'test'
