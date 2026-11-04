import pytest
from traffic_fine import speeding_fine, license_action, total_penalty


# Speeding fine tests
def test_no_speeding():
    assert speeding_fine(50, 60, "city") == 0

def test_school_zone():
    assert speeding_fine(70, 60, "school") == 2000

def test_highway_zone():
    assert speeding_fine(70, 60, "highway") == 1000

def test_other_zone():
    assert speeding_fine(70, 60, "city") == 500

def test_excess_above_40():
    assert speeding_fine(105, 60, "school") == 6000

def test_excess_above_20():
    assert speeding_fine(85, 60, "highway") == 2000


# Licence action tests
def test_commercial_revoke():
    assert license_action(12, True, False) == "revoke"

def test_non_commercial_suspend():
    assert license_action(12, False, False) == "suspend"

def test_repeat_offender_suspend():
    assert license_action(8, False, True) == "suspend"

def test_warning():
    assert license_action(8, False, False) == "warning"

def test_notice():
    assert license_action(4, False, False) == "notice"


# Total penalty tests
def test_total_penalty():
    assert total_penalty([1000, 2000, 3000]) == 6000

def test_penalty_cap():
    assert total_penalty([6000, 7000]) == 10000

def test_negative_fine():
    with pytest.raises(ValueError):
        total_penalty([1000, -500])

def test_empty_fines():
    assert total_penalty([]) == 0

def test_clean_record():
    assert license_action(2, False, False) == "none"