import pytest

from cssselect.xpath import ExpressionError

from lxml.etree import XPathEvalError

from pat import pat


def test_valid_css(html_blob):
    """Ensures a valid XPath produces results
    """

    # extract only the first table
    css_query = '.maintext .night'
    results = pat(html_blob, css_query=css_query)
    assert len(results) == 1
    assert results[0].text_content() == 'LIGHTS: 1988'


def test_invalid_css(html_blob):
    """Ensures an invalid XPath halts execution
    """

    css_query = '.maintext .night::text'

    with pytest.raises(ExpressionError):
        results = pat(html_blob, css_query=css_query)
