import sys
sys.path.append('.')
from settings import *

EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
    }

STATIC_EXCLUDE_SOURCES = False

RELATIVE_URLS = False

CSS_MIN = True
HTML_MIN = True
INLINE_CSS_MIN = True
INLINE_JS_MIN = True