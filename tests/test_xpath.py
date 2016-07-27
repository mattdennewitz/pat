import pytest

from lxml.etree import XPathEvalError

from pat import pat


def test_valid_xpath(html_blob):
    """Ensures a valid XPath produces results
    """

    # extract only the first table
    xpath = '/descendant::table[1]'
    results = pat(html_blob, xpath_query=xpath)

    assert len(results) == 1


def test_invalid_xpath(html_blob):
    """Ensures an invalid XPath halts execution
    """

    # invalid xpath
    invalid_xpath = '/descendant:table[1]'

    with pytest.raises(XPathEvalError):
        pat(html_blob, xpath_query=invalid_xpath)
