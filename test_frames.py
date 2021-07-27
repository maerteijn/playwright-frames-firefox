import os

CURRENT_PATH = os.path.realpath('.')


def test_page_without_script_file(page):
    page.goto(f"file://{CURRENT_PATH}/public/index-without-script.html")

    iframe = page.frame("iframe")
    iframe_with_selector = page.query_selector("iframe").content_frame()

    assert iframe_with_selector is not None
    assert len(page.frames) == 2
    assert iframe.url.endswith("iframe.html")


def test_page_with_script_file(page):
    page.goto(f"file://{CURRENT_PATH}/public/index-with-script.html")

    iframe = page.frame("iframe")
    iframe_with_selector = page.query_selector("iframe").content_frame()

    assert iframe_with_selector is not None
    assert len(page.frames) == 2
    assert iframe.url.endswith("iframe.html")


def test_page_with_script_script_included_file(page):
    page.goto(f"file://{CURRENT_PATH}/public/index-with-script-included.html")

    iframe = page.frame("iframe")
    iframe_with_selector = page.query_selector("iframe").content_frame()

    assert iframe_with_selector is not None
    assert len(page.frames) == 2
    assert iframe.url.endswith("iframe.html")


def test_page_without_script_localhost(page):
    page.goto("http://localhost:8000/index-without-script.html")

    iframe = page.frame("iframe")
    iframe_with_selector = page.query_selector("iframe").content_frame()

    assert iframe_with_selector is not None
    assert len(page.frames) == 2
    assert iframe.url.endswith("iframe.html")


def test_page_with_script_localhost(page):
    page.goto("http://localhost:8000/index-with-script.html")

    iframe = page.frame("iframe")
    iframe_with_selector = page.query_selector("iframe").content_frame()

    assert iframe_with_selector is not None
    assert len(page.frames) == 2
    assert iframe.url.endswith("iframe.html")
