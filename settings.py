# -*- coding: utf-8 -*-
LOCALE = ('en_US',)
DEFAULT_DATE_FORMAT = '%-d/%-m/%Y'

AUTHOR = u'Aquiles Carattino'
SITENAME = u'Python For The Lab'
SITEURL = u'http://localhost:8000'
TIMEZONE = 'Europe/Amsterdam'

TEMPLATE_PAGES = {
    'static_index.html': 'index.html',
    'books.html': 'books/index.html',
    'about.html': 'about/index.html',
    'hire_me.html': 'hire-me/index.html',
    '404.html': '404.html',
    }

STATIC_PATHS = ['images', 'static']
STATIC_EXCLUDE_SOURCES = False

ARTICLE_URL = 'blog/{slug}'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'

PAGE_SAVE_AS = '{slug}/index.html'

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.9,
        'indexes': 0.5,
        'pages': 0.5
        },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'weekly',
        'pages': 'monthly'
        },
    'exclude': ['tag/', 'category/', 'categories.html', 'tags.html', 'search/'],
    }

FEED_DOMAIN = 'https://www.pythonforthelab.com'
FEED_RSS = 'feed.rss'

# MARKUP = ('rst', 'markdown',)

RELATIVE_URLS = True

INDEX_SAVE_AS = 'blog/index.html'

DEFAULT_PAGINATION = 10

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.fenced_code': {},
        'markdown.extensions.admonition': {},
        },
    'output_format': 'html5',
    }

SIMILAR_POSTS_MAX_COUNT = 3

CSS_MIN = False
HTML_MIN = False
JS_MIN = False
INLINE_CSS_MIN = False
INLINE_JS_MIN = False
