"""Utility functions for calculating Pflegegrad scores."""
from typing import Dict

from config.pflegegrad_config import pflegegrad_thresholds

# Mapping tables copied from app.py
weighted_score_mapping_tables = {
    1: [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 10), (12, 10), (13, 10), (14, 10), (15, 10)],
    2: [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 15), (17, 15), (18, 15), (19, 15), (20, 15), (21, 15), (22, 15), (23, 15), (24, 15), (25, 15), (26, 15), (27, 15), (28, 15), (29, 15), (30, 15), (31, 15), (32, 15), (33, 15)],
    3: [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (10, 10), (11, 10), (12, 10), (13, 10), (14, 10), (15, 15), (16, 15), (17, 15), (18, 15), (19, 15), (20, 15), (21, 15), (22, 15), (23, 15), (24, 15), (25, 15), (26, 15), (27, 15), (28, 15), (29, 15), (30, 15), (31, 15), (32, 15), (33, 15), (34, 15), (35, 15), (36, 15), (37, 15), (38, 15), (39, 15), (40, 15), (41, 15), (42, 15), (43, 15), (44, 15), (45, 15), (46, 15), (47, 15), (48, 15), (49, 15), (50, 15), (51, 15), (52, 15), (53, 15), (54, 15), (55, 15), (56, 15), (57, 15), (58, 15), (59, 15), (60, 15), (61, 15), (62, 15), (63, 15), (64, 15), (65, 15)],
    4: [(0, 0), (1, 2.5), (2, 5), (3, 7.5), (4, 10), (5, 12.5), (6, 15), (7, 17.5), (8, 20), (9, 22.5), (10, 25), (11, 27.5), (12, 30), (13, 32.5), (14, 35), (15, 37.5), (16, 40), (17, 40), (18, 40), (19, 40), (20, 40), (21, 40), (22, 40), (23, 40), (24, 40), (25, 40), (26, 40), (27, 40), (28, 40), (29, 40), (30, 40), (31, 40), (32, 40), (33, 40), (34, 40), (35, 40), (36, 40), (37, 40), (38, 40), (39, 40), (40, 40), (41, 40), (42, 40), (43, 40), (44, 40), (45, 40), (46, 40), (47, 40), (48, 40)],
     # Modul 5 laut NBA
    5: [
        (0, 0),
        (1, 5),
        (2, 10), (3, 10),
        (4, 15), (5, 15),
        (6, 20)
    ],
    6: [(0, 0), (1, 1.25), (2, 2.5), (3, 3.75), (4, 5), (5, 6.25), (6, 7.5), (7, 8.75), (8, 10), (9, 11.25), (10, 12.5), (11, 13.75), (12, 15), (13, 15), (14, 15), (15, 15), (16, 15), (17, 15), (18, 15)],
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