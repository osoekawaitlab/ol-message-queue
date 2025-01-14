import re

import olmq


def test_package_has_versoin() -> None:
    assert re.match(r"\d+\.\d+\.\d+", olmq.__version__)
