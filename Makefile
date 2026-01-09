run:
	pelican -t theme -s settings.py -o output/ content

publish:
	pelican -t theme -s settings_publish.py -o output/ content
