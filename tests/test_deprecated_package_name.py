"""Test that the former name of this package `pytest-artifact` (without the 's')
is deprecated and raises a warning when used.
"""

import pytest

pytest_artifact = pytest.importorskip("pytest_artifact")


def test_pytest_artifact_raises_deprecation_warning(pytester):
    """Test that importing pytest_artifact raises a deprecation warning."""
    pytester.makepyfile("""
        def test_something(artifacts):
            assert artifacts.__module__.split(".")[0] == "pytest_artifact"
    """)

    result = pytester.runpytest("-v")
    assert result.parseoutcomes() == {"passed": 1, "warnings": 1}
    result.stdout.fnmatch_lines(
        [
            "*::test_something PASSED*",
            "*DeprecationWarning*`pytest-artifact`*deprecated*`pytest-artifacts`*",
        ]
    )
