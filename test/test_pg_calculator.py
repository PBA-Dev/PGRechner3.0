from pathlib import Path
import sys
import pytest

# Ensure the project root is on sys.path so that imports work when running tests
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from config.pg_calculator import (
    map_raw_to_weighted_score,
    total_weighted_score,
    determine_pflegerad,
    calculate_pflegerad,
)


def test_map_raw_to_weighted_score():
    assert map_raw_to_weighted_score(1, 6) == 7.5
    assert map_raw_to_weighted_score(2, 11) == 11.25
    assert map_raw_to_weighted_score(3, 5) == 11.25
    assert map_raw_to_weighted_score(4, 19) == 30
    assert map_raw_to_weighted_score(5, 1) == 5
    assert map_raw_to_weighted_score(6, 4) == 7.5


def test_total_weighted_score():
    raw_scores = {1: 6, 2: 11, 3: 5, 4: 20, 5: 1, 6: 4}
    expected = 61.25
    assert total_weighted_score(raw_scores) == pytest.approx(expected)


def test_determine_pflegerad():
    assert determine_pflegerad(61.25) == 3
    assert determine_pflegerad(10) == 0
    assert determine_pflegerad(75) == 4


def test_calculate_pflegerad():
    raw_scores = {1: 6, 2: 11, 3: 5, 4: 20, 5: 1, 6: 4}
    result = calculate_pflegerad(raw_scores)
    assert result["total_score"] == pytest.approx(61.25)
    assert result["pflegegrad"] == 3
    