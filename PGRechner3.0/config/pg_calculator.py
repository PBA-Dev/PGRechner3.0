"""Utility functions for calculating Pflegegrad scores."""
from typing import Dict

from config.pflegegrad_config import pflegegrad_thresholds

# Mapping tables copied from app.py
weighted_score_mapping_tables = {
    # Module 1
    1: [
        (0, 0),
        (2, 2.5),
        (4, 5),
        (6, 7.5),
        (10, 10),
    ],
    # Module 2
    2: [
        (0, 0),
        (2, 3.75),
        (6, 7.5),
        (11, 11.25),
        (17, 15),
    ],
    # Module 3
    3: [
        (0, 0),
        (1, 3.75),
        (3, 7.5),
        (5, 11.25),
        (7, 15),
    ],
    # Module 4
    4: [
        (0, 0),
        (3, 10),
        (8, 20),
        (19, 30),
        (37, 40),
    ],
    # Modul 5 laut NBA
    5: [
        (0, 0),
        (1, 5),
        (2, 10),
        (4, 15),
        (6, 20),
    ],
    # Module 6
    6: [
        (0, 0),
        (1, 3.75),
        (4, 7.5),
        (7, 11.25),
        (12, 15),
    ],
        }


def map_raw_to_weighted_score(module_id: int, raw_score: float) -> float:
    """Convert raw module points to weighted points using the official tables."""
    mapping = weighted_score_mapping_tables.get(module_id, [])
    weighted = 0.0
    for limit, value in mapping:
        if raw_score >= limit:
            weighted = value
        else:
            break
    return float(weighted)


def total_weighted_score(raw_scores: Dict[int, float]) -> float:
    """Calculate the overall weighted score from raw scores."""
    m1 = map_raw_to_weighted_score(1, raw_scores.get(1, 0))
    m2 = map_raw_to_weighted_score(2, raw_scores.get(2, 0))
    m3 = map_raw_to_weighted_score(3, raw_scores.get(3, 0))
    m4 = map_raw_to_weighted_score(4, raw_scores.get(4, 0))
    m5 = map_raw_to_weighted_score(5, raw_scores.get(5, 0))
    m6 = map_raw_to_weighted_score(6, raw_scores.get(6, 0))

    score = m1
    score += max(m2, m3)  # only the higher of module 2 or 3 counts
    score += m4 + m5 + m6
    return score


def determine_pflegerad(total_score: float) -> int:
    """Return the Pflegegrad based on the configured thresholds."""
    grad = 0
    for level, cfg in sorted(pflegegrad_thresholds.items(), key=lambda x: x[1]['min_points']):
        if total_score >= cfg['min_points']:
            grad = level
        else:
            break
    return grad


def calculate_pflegerad(raw_scores: Dict[int, float]) -> Dict[str, float | int]:
    """Convenience helper returning score and grade."""
    score = total_weighted_score(raw_scores)
    grade = determine_pflegerad(score)
    return {
        'total_score': round(score, 2),
        'pflegegrad': grade,
    }
