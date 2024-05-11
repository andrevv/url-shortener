from src import logic


def test_to_short_and_to_original():
    url = 'https://example.com'
    short_url = logic.to_short(url)
    original_url = logic.to_original(short_url)
    assert original_url == url
