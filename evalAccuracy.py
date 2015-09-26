import requests

def lookUp(thing):
	result = []
	url = 'http://conceptnet5.media.mit.edu/data/5.4/c/en/' + thing
	object_dictionary = requests.get(url).json()
	print(object_dictionary['edges'])
	print(type(object_dictionary['edges']))
	for val in object_dictionary['edges']:
		if 'IsA' in val['uri'] and '/v/' not in val['uri']:
			temp = val['uri']
			tempList = readDef(temp)
			for val in tempList:
				if val not in result:
					result.append(val)
	return result

def readDef(value):
	result = []
	for index in range(len(value)):
		if value[index:index + 6] == '/c/en/':
			tempString = ""
			tempIndex = index + 6
			index += 6
			print(value[tempIndex:])
			print(tempIndex)
			while value[tempIndex] != "/":
				if value[tempIndex] == "_":
					tempString += " "
				else: 
					tempString += value[tempIndex]
				tempIndex += 1
			result.append(tempString)
	return result

print(lookUp('saxophone'))

