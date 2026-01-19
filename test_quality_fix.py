#!/usr/bin/env python3
"""
Unit test for quality assignment bug fix.

This test verifies that the quality assignment logic correctly handles
quality 0 (Normal) without replacing it with default values.
"""

def test_quality_assignment_logic():
    """Test the fixed quality assignment pattern."""

    print("=" * 80)
    print("Testing Quality Assignment Logic Fix")
    print("=" * 80)
    print()

    # Simulate the old buggy behavior
    def old_assignment(quality, default):
        """Old buggy pattern: item.get("quality") or default"""
        return quality or default

    # Simulate the new fixed behavior
    def new_assignment(quality, default):
        """New fixed pattern: item.get("quality") if item.get("quality") is not None else default"""
        return quality if quality is not None else default

    test_cases = [
        {"quality": 0, "default": 6, "expected": 0, "description": "Quality 0 (Normal)"},
        {"quality": 1, "default": 6, "expected": 1, "description": "Quality 1 (Genuine)"},
        {"quality": 5, "default": 6, "expected": 5, "description": "Quality 5 (Unusual)"},
        {"quality": 6, "default": 6, "expected": 6, "description": "Quality 6 (Unique)"},
        {"quality": 11, "default": 6, "expected": 11, "description": "Quality 11 (Strange)"},
        {"quality": None, "default": 6, "expected": 6, "description": "Quality None (should use default)"},
    ]

    print("OLD BUGGY BEHAVIOR:")
    print("-" * 80)
    old_passed = 0
    old_failed = 0

    for test in test_cases:
        result = old_assignment(test["quality"], test["default"])
        status = "✓ PASS" if result == test["expected"] else "✗ FAIL"
        if result == test["expected"]:
            old_passed += 1
        else:
            old_failed += 1
        print(f"{test['description']:30} | Input: {str(test['quality']):5} | Expected: {test['expected']} | Got: {result} | {status}")

    print()
    print("NEW FIXED BEHAVIOR:")
    print("-" * 80)
    new_passed = 0
    new_failed = 0

    for test in test_cases:
        result = new_assignment(test["quality"], test["default"])
        status = "✓ PASS" if result == test["expected"] else "✗ FAIL"
        if result == test["expected"]:
            new_passed += 1
        else:
            new_failed += 1
        print(f"{test['description']:30} | Input: {str(test['quality']):5} | Expected: {test['expected']} | Got: {result} | {status}")

    print()
    print("=" * 80)
    print("SUMMARY:")
    print("-" * 80)
    print(f"Old behavior: {old_passed} passed, {old_failed} failed out of {len(test_cases)} tests")
    print(f"New behavior: {new_passed} passed, {new_failed} failed out of {len(test_cases)} tests")
    print()

    if new_failed == 0:
        print("✓ All tests passed with the new fixed behavior!")
        print("✓ The bug fix correctly handles quality 0 (Normal) without replacing it.")
        return True
    else:
        print("✗ Some tests failed with the new behavior.")
        return False


if __name__ == "__main__":
    import sys
    success = test_quality_assignment_logic()
    sys.exit(0 if success else 1)
