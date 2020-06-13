""" In re: package expectations.
"""
import semantic_version

import reflection


def test_namespace():
    assert reflection.__name__ == "reflection"


def test_version():
    assert semantic_version.validate(reflection.__version__)
