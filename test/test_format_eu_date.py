from pathlib import Path
import sys
import os
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

os.environ.setdefault("DATABASE_URL", "sqlite:///:memory:")

from app import format_eu_date


def test_format_eu_date_date_only():
    assert format_eu_date("2023-10-05") == "05.10.2023"


def test_format_eu_date_datetime_space():
    assert format_eu_date("2023-10-05 13:45:30") == "05.10.2023 13:45:30"


def test_format_eu_date_invalid():
    assert format_eu_date("notadate") == "notadate"