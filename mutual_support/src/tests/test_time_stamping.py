from datetime import datetime, timedelta
from unittest.mock import Mock

import pytest

from mutual_support.src.time_stamping import APITimestamp


@pytest.fixture
def api_timestamp():
    mock_api = Mock()
    mock_api.fetch_data.return_value = {'list': []}
    return APITimestamp(mock_api)


class TestTimeStamping:
    def test_timestamping_is_not_none(self, api_timestamp):
        assert api_timestamp.stamp is not None

    def test_timestamping_is_datetime(self, api_timestamp):
        assert isinstance(api_timestamp.stamp, datetime)

    def test_is_expired(self, api_timestamp):
        assert not api_timestamp.is_expired()

        api_timestamp.stamp -= timedelta(minutes=11)
        assert api_timestamp.is_expired()
