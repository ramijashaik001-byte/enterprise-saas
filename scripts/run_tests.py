import pytest
import sys
import traceback

def main():
    print("Running pytest and capturing tracebacks...")
    try:
        # Run pytest programmatically with verbose tracebacks
        pytest.main(["tests/test_tenant.py", "-vv", "--tb=long"])
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
