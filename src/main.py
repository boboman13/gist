#!/usr/bin/env python
# Gisting library

import requests
import json
import os

from subprocess import call

gistfile = "./gistfile.tmp"

# Uploads the gist
def uploadGist(description, text):
	payload = {
		'files': {
			'file1': {
				'content': text
			}
		},
		'public': True,
		'description': description
	}

	r = requests.post("https://api.github.com/gists", data=json.dumps(payload))
	return r.json()['html_url']

# Gets the contents of the .gistfile.tmp
def getGistfile():
	with open(gistfile, "r") as file:
		return file.read().replace('\n', '')

# Lets gist this!
# TODO: make editor configurable
call(["nano", gistfile])

gistData = getGistfile()

# read line
desc = raw_input('  Please enter a description for this gist: ')

print('  Uploaded to ' + uploadGist(desc, gistData))

# clean up
os.remove(gistfile)
