import os

import pytest


FIXTURES_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__),
                                             'fixtures'))


@pytest.fixture
def html_blob():
    return open(os.path.join(FIXTURES_DIR, 'park.html'), 'r').read()
