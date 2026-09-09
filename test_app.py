import os
from unittest.mock import patch

import app


@patch.dict(os.environ, {"YT_COOKIES_FROM_BROWSER": "chrome"}, clear=False)
def test_browser_cookie_option_is_enabled():
    options = app.get_yt_dlp_options()
    assert options["cookiesfrombrowser"] == ("chrome",)


@patch.dict(os.environ, {"YT_COOKIE_FILE": "/tmp/cookies.txt"}, clear=False)
def test_cookie_file_option_is_enabled():
    options = app.get_yt_dlp_options()
    assert options["cookies"] == "/tmp/cookies.txt"
