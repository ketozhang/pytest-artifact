import warnings

DEPRECATED_PACKAGE_NAME_WARNING_MSG = (
    " This package, `pytest-artifact`, is deprecated and has been renamed to"
    " `pytest-artifacts`. No new versions will be released under the old name."
    " Please install `pytest-artifacts` instead."
)


def raise_deprecated_package_name_warning():
    warnings.warn(DEPRECATED_PACKAGE_NAME_WARNING_MSG, DeprecationWarning, stacklevel=2)


raise_deprecated_package_name_warning()
