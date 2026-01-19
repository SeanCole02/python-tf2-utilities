#!/usr/bin/env python3
"""
Test for Normal quality SKU conversion bug fix.

This test verifies that items with "Normal" quality (quality ID 0) are correctly
parsed and converted to SKU format, rather than being incorrectly assigned quality 6.
"""

import sys
import os

# Add parent directory to path to import tf2utilities
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tf2utilities.schema import Schema
from tf2utilities.sku import SKU
import json

def test_normal_quality_sku_conversion():
    """Test that Normal quality items are correctly converted to SKU with quality 0."""

    print("=" * 80)
    print("Testing Normal Quality SKU Conversion")
    print("=" * 80)

    # Test cases with expected SKU outputs
    test_cases = [
        {
            "name": "Strange Normal Professional Killstreak Scattergun",
            "expected_sku": "200;0;strange;kt-3",
            "description": "Strange with Normal quality and killstreak"
        },
        {
            "name": "Normal Scattergun",
            "expected_sku": "200;0",
            "description": "Simple Normal quality item"
        },
        {
            "name": "Strange Normal Killstreak Scattergun",
            "expected_sku": "200;0;strange;kt-1",
            "description": "Strange Normal with basic killstreak"
        },
        {
            "name": "Strange Normal Specialized Killstreak Scattergun",
            "expected_sku": "200;0;strange;kt-2",
            "description": "Strange Normal with specialized killstreak"
        },
    ]

    # Load schema backup for testing
    print("\nLoading schema backup...")
    schema_data = Schema.loadBackup()

    if not schema_data:
        print("ERROR: No schema backup found. Please run the application to create a schema backup first.")
        print("You can create one by fetching schema data using the tf2utilities API.")
        return False

    schema = Schema(schema_data)
    print("Schema loaded successfully!\n")

    # Run test cases
    passed = 0
    failed = 0

    for i, test in enumerate(test_cases, 1):
        print(f"Test {i}: {test['description']}")
        print(f"  Input name: {test['name']}")
        print(f"  Expected SKU: {test['expected_sku']}")

        # Get item object from name
        item_obj = schema.getItemObjectFromName(test['name'])

        # Convert to SKU
        actual_sku = SKU.fromObject(item_obj)

        print(f"  Actual SKU: {actual_sku}")
        print(f"  Item object quality: {item_obj.get('quality')}")

        # Check if it matches expected
        if actual_sku == test['expected_sku']:
            print("  ✓ PASSED")
            passed += 1
        else:
            print("  ✗ FAILED")
            print(f"    Item object: {json.dumps(item_obj, indent=4)}")
            failed += 1
        print()

    # Summary
    print("=" * 80)
    print(f"Test Summary: {passed} passed, {failed} failed out of {len(test_cases)} total")
    print("=" * 80)

    return failed == 0


if __name__ == "__main__":
    try:
        success = test_normal_quality_sku_conversion()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\nERROR: Test execution failed with exception:")
        print(f"{type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
