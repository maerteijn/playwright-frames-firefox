# playwright-frames-firefox
A test repo to demonstrate some weird behaviour with iframes and the firefox browser


## Introduction

A script tag causes that iframes are not queried / available when using firefox as a browser. When using
chromium, all seems fine.

The testsuite in [test_frames.py](https://github.com/maerteijn/playwright-frames-firefox/blob/main/test_frames.py) is testing two HTML pages which both contain an iframe: One of the pages also has a `<script>` tag, the other one has not.

On the page with the script tag thhe iframe is not available in `page.frames` or with `page.frame("iframe")`. The element is queryable using `query_selecter`, but then `content_frame()` return `None`.

## Run the tests

How to run the testsuite (recommended to run inside a virtualenv):

```bash
pip install -r requirements.txt

# run with chromium
 pytest -s test_frames.py --headed --browser=chromium

# run with firefox
 pytest -s test_frames.py --headed --browser=firefox
```

This was tested with python 3.9 on Mac OS 10.14.6, also with [Github Actions with Ubuntu 20.04](https://github.com/maerteijn/playwright-frames-firefox/runs/3163061903?check_suite_focus=true)
