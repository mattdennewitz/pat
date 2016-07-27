from lxml.cssselect import CSSSelector
from lxml import html


__all__ = ('pat', )

def pat(data, xpath_query=None, css_query=None):
    """Queries file data using given XPath or CSS selector,
    returns results.

    Args:
        data: String of HTML to be parsed, queried. Required.
        xpath_query: Valid XPath query. Required if `css_query` is not given.
        css_query: CSS selector path. Required when `xpath_query` not given.

    Returns:
        List of nodes found for query
    """

    doc = html.fromstring(data)

    if xpath_query:
        return doc.xpath(xpath_query)

    css = CSSSelector(css_query)
    return css(doc)
