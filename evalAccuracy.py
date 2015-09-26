import requests

def lookUp(thing):
	url = 'http://conceptnet5.media.mit.edu/data/5.4/c/en/' + thing
	object_dictionary = requests.get(url).json()
	return object_dictionary

print(lookUp('toast'))