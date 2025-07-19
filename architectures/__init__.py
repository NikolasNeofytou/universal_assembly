"""Architecture package for Universal Assembly."""

from . import x86, arm

ARCHS = {
    "x86": x86.FEATURES,
    "arm": arm.FEATURES,
}


def get_arch(name: str):
    """Return feature dictionary for the given architecture name."""
    return ARCHS.get(name)
