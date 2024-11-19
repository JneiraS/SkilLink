import pytest

from mutual_support.src.api import WeatherAPI


@pytest.fixture
def sample_weather_data():
    return {
        'list': [
            {
                'dt_txt': '2024-01-01 12:00:00',
                'weather': [{'main': 'Rain'}]
            },
            {
                'dt_txt': '2024-01-01 15:00:00',
                'weather': [{'main': 'Rain'}]
            },
            {
                'dt_txt': '2024-01-02 12:00:00',
                'weather': [{'main': 'Clear'}]
            },
            {
                'dt_txt': '2024-01-03 12:00:00',
                'weather': [{'main': 'Rain'}]
            },
            {
                'dt_txt': '2024-01-04 12:00:00',
                'weather': [{'main': 'Clouds'}]
            }
        ]
    }


class TestGetRainyDays:
    def test_get_rainy_days_returns_set(self, sample_weather_data):
        result = WeatherAPI.get_rainy_days(sample_weather_data)
        assert isinstance(result, set)

    def test_get_rainy_days_correct_dates(self, sample_weather_data):
        result = WeatherAPI.get_rainy_days(sample_weather_data)
        assert result == {'2024-01-01', '2024-01-03'}

    def test_get_rainy_days_empty_data(self):
        empty_data = {'list': []}
        result = WeatherAPI.get_rainy_days(empty_data)
        assert result == set()

    def test_get_rainy_days_no_rain(self):
        no_rain_data = {
            'list': [
                {
                    'dt_txt': '2024-01-01 12:00:00',
                    'weather': [{'main': 'Clear'}]
                },
                {
                    'dt_txt': '2024-01-02 12:00:00',
                    'weather': [{'main': 'Clouds'}]
                }
            ]
        }
        result = WeatherAPI.get_rainy_days(no_rain_data)
        assert result == set()

    def test_get_rainy_days_same_day_multiple_rain(self, sample_weather_data):
        result = WeatherAPI.get_rainy_days(sample_weather_data)
        assert len(result) == 2
        assert '2024-01-01' in result
