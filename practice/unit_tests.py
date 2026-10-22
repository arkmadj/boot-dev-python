run_cases: list[dict[str, list[int] | float]] = [
    {
        "luck_boosts": [5, 3, 10],
        "expected_avg": 6.0,
    },
    {
        "luck_boosts": [7],
        "expected_avg": 7.0,
    },
    {
        "luck_boosts": [4, 4, 4],
        "expected_avg": 4.0,
    },
    {
        "luck_boosts": [2, 3],
        "expected_avg": 2.5,
    },
    {
        "luck_boosts": [],
        "expected_avg": 0.0,
    },
]

def avg_luck_boost(luck_boosts: list[int]) -> float:
    if not list:
        return 0.0
    total = 0
    for boost in luck_boosts:
        total += boost
    return total / len(luck_boosts)


from math import isclose
import pytest

@pytest.mark.parametrize("case", run_cases)
def test_avg_luck_boost(case):
    print("\n---------------------------------")
    luck_boosts = case["luck_boosts"]
    expected_avg = case["expected_avg"]
    print(f"Party luck boosts: {luck_boosts}")

    assert isinstance(luck_boosts, list)
    assert isinstance(expected_avg, float)

    avg = avg_luck_boost(luck_boosts)
    print(f"Expected average boost: {expected_avg}")
    print(f"Actual average boost:   {avg}")
    assert isclose(avg, expected_avg)

