import os

CURRENT_PATH = os.path.realpath('.')


def test_page_without_script(page):
    page.goto("file://{}/index-without-script.html".format(CURRENT_PATH))
    iframe = page.frame("iframe")
    iframe_with_selector = page.query_selector("iframe").content_frame()

    assert iframe_with_selector is not None
    assert len(page.frames) == 2
    assert iframe.url.endswith("iframe.html")


def test_page_with_script(page):
    page.goto("file://{}/index-with-script.html".format(CURRENT_PATH))

    iframe = page.frame("iframe")
    iframe_with_selector = page.query_selector("iframe").content_frame()

    assert iframe_with_selector is not None
    assert len(page.frames) == 2
    assert iframe.url.endswith("iframe.html")
