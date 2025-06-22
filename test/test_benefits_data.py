from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from config.benefits_data import pflegegrad_benefits


def test_all_pflegegrade_present():
    for pg in range(6):
        assert pg in pflegegrad_benefits


def test_leistungen_have_required_fields():
    for pg_data in pflegegrad_benefits.values():
        for period in ("period_1", "period_2"):
            assert period in pg_data
            period_data = pg_data[period]
            assert "leistungen" in period_data
            assert isinstance(period_data["leistungen"], list)
            for entry in period_data["leistungen"]:
                assert "name" in entry
                assert "value" in entry