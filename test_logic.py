from helpers.logic import wikiData


def test_wikiData():
    assert "1949" in wikiData()
