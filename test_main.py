"""Модульные тесты к кейс-задаче № 1. Запуск: python -m unittest -v"""

import unittest
from datetime import date

from main import (
    calculate_age,
    days_in_month,
    format_date_as_display,
    is_leap_year,
    render_number,
    weekday_name,
    DIGIT_HEIGHT,
)


class TestLeapYear(unittest.TestCase):
    def test_divisible_by_four(self):
        self.assertTrue(is_leap_year(2024))
        self.assertTrue(is_leap_year(1996))

    def test_century_not_leap(self):
        self.assertFalse(is_leap_year(1900))
        self.assertFalse(is_leap_year(2100))

    def test_divisible_by_four_hundred(self):
        self.assertTrue(is_leap_year(2000))
        self.assertTrue(is_leap_year(1600))

    def test_ordinary_year(self):
        self.assertFalse(is_leap_year(2023))


class TestDaysInMonth(unittest.TestCase):
    def test_february(self):
        self.assertEqual(days_in_month(2, 2024), 29)
        self.assertEqual(days_in_month(2, 2023), 28)

    def test_thirty_and_thirty_one(self):
        self.assertEqual(days_in_month(4, 2023), 30)
        self.assertEqual(days_in_month(12, 2023), 31)


class TestWeekday(unittest.TestCase):
    """Контрольные даты сверены со стандартной библиотекой."""

    def test_known_dates(self):
        cases = [
            (12, 4, 1961, "среда"),      # полёт Ю. А. Гагарина
            (1, 1, 2000, "суббота"),
            (9, 5, 1945, "среда"),
            (29, 2, 2024, "четверг"),    # високосный день
        ]
        for day, month, year, expected in cases:
            with self.subTest(date=(day, month, year)):
                self.assertEqual(weekday_name(day, month, year), expected)

    def test_matches_standard_library(self):
        names = (
            "понедельник", "вторник", "среда", "четверг",
            "пятница", "суббота", "воскресенье",
        )
        for ordinal in range(date(1990, 1, 1).toordinal(), date(2030, 1, 1).toordinal()):
            d = date.fromordinal(ordinal)
            self.assertEqual(
                weekday_name(d.day, d.month, d.year),
                names[d.weekday()],
                msg=f"расхождение на дате {d}",
            )


class TestAge(unittest.TestCase):
    def test_before_birthday(self):
        self.assertEqual(calculate_age(1, 6, 2000, today=date(2024, 5, 31)), 23)

    def test_on_birthday(self):
        self.assertEqual(calculate_age(1, 6, 2000, today=date(2024, 6, 1)), 24)

    def test_after_birthday(self):
        self.assertEqual(calculate_age(1, 6, 2000, today=date(2024, 12, 31)), 24)

    def test_leap_day_birth(self):
        self.assertEqual(calculate_age(29, 2, 2000, today=date(2023, 3, 1)), 23)


class TestRender(unittest.TestCase):
    def test_height(self):
        self.assertEqual(len(render_number("2024").split("\n")), DIGIT_HEIGHT)

    def test_all_digits_supported(self):
        output = render_number("0123456789")
        self.assertEqual(len(output.split("\n")), DIGIT_HEIGHT)
        self.assertIn("*", output)

    def test_full_date_line_count(self):
        self.assertEqual(
            len(format_date_as_display(9, 5, 1945).split("\n")), DIGIT_HEIGHT
        )


if __name__ == "__main__":
    unittest.main()
