PREFIX ?= /usr/bin

install:
	pip install requests
	cp ./src/main.py $(PREFIX)/gist
	chmod +x $(PREFIX)/gist
	echo "Installed. Use as \"gist\" in command line."

uninstall:
	rm -f $(PREFIX)/gist
	echo "Uninstalled from $(PREFIX)/gist".
