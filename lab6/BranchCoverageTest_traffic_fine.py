import pytest
from traffic_fine import speeding_fine, license_action, total_penalty


# Speeding fine – branch tests
def test_speed_within_limit():
    assert speeding_fine(50, 60, "city") == 0

def test_speed_above_limit():
    assert speeding_fine(70, 60, "city") == 500

def test_school_zone():
    assert speeding_fine(70, 60, "school") == 2000

def test_highway_zone():
    assert speeding_fine(70, 60, "highway") == 1000

def test_excess_above_40():
    assert speeding_fine(105, 60, "school") == 6000

def test_excess_between_21_and_40():
    assert speeding_fine(85, 60, "highway") == 2000

def test_excess_20_or_less():
    assert speeding_fine(80, 60, "city") == 500


# Licence action – branch tests
def test_12_points_commercial():
    assert license_action(12, True, False) == "revoke"

def test_12_points_non_commercial():
    assert license_action(12, False, False) == "suspend"

def test_8_points_repeat_offender():
    assert license_action(8, False, True) == "suspend"

def test_8_points_first_offender():
    assert license_action(8, False, False) == "warning"

def test_4_points():
    assert license_action(4, False, False) == "notice"

def test_below_4_points():
    assert license_action(2, False, False) == "none"


# Total penalty – branch tests
def test_normal_total():
    assert total_penalty([1000, 2000, 3000]) == 6000

def test_empty_fines():
    assert total_penalty([]) == 0

def test_negative_fine():
    with pytest.raises(ValueError):
        total_penalty([1000, -500])

def test_penalty_above_limit():
    assert total_penalty([6000, 7000]) == 10000

def test_penalty_below_limit():
    assert total_penalty([1000, 2000]) == 3000