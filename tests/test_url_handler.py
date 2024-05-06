from src import url_handler


def test_to_short_and_to_original():
    url = 'https://example.com'
    short_url = url_handler.to_short(url)
    original_url = url_handler.to_original(short_url)
    assert original_url == url
