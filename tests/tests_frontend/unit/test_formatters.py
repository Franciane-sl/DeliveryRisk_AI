import pytest

from frontend.utils.formatters import format_percentage, format_datetime

class TestFormatPercentage:

    @pytest.mark.parametrize(
        "value, expected",
        [
            (0.4269, "42.69%"),
            (0.5145, "51.45%"),
            (0.0, "0.00%"),
            (1.0, "100.00%"),
            (0.5, "50.00%"),
        ],
    )
    def test_format_percentage(self, value, expected):
        assert format_percentage(value) == expected


class TestFormatDatetime:

    def test_format_datetime_valid(self):
        resultado = format_datetime("2026-11-03T10:30:00")

        assert resultado == "03/11/2026 10:30:00"

    def test_format_datetime_with_timezone_z(self):
        resultado = format_datetime("2026-11-03T10:30:00Z")

        assert resultado == "03/11/2026 10:30:00"

    def test_format_datetime_invalid(self):
        valor = "data_invalida"

        assert format_datetime(valor) == valor

    def test_format_datetime_empty(self):
        assert format_datetime("") == ""

    def test_format_datetime_none(self):
        assert format_datetime(None) is None
